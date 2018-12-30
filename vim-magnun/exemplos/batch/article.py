#!/usr/bin/env python3
# encoding: utf-8
#
# Folios - Yet Another Static Site Generator
# Copyright (C) 2015 - Magnun Leno
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import re
import copy
import base64
import docutils
import docutils.core

from functools import partial
from datetime import datetime
from docutils.writers.html4css1 import HTMLTranslator

from folios.core import utils
from folios.core import logger
from folios.core import exceptions as e
from folios.core.indexes import ArticlesIndex
from folios.core.contents import GenericContent
from folios.core.contents import Image

class ArticleTranslator(HTMLTranslator):
	def __init__(self, document, article):
		super().__init__(document)
		self.article = article

	def visit_image(self, node):
		image_src_path = os.path.join(utils.resolve_root_folder(), node['uri'])
		if not image_src_path.startswith("/"):
			image_src_path = "/" + image_src_path

		image = Image.__all__.get(image_src_path, None)
		if image is None:
			self.article.log.warning(
				"Image not found in images folder: {}".format(
					utils.get_better_path_rep(image_src_path)
				)
			)
		else:
			node['uri'] = image.url

		if 'alt' not in node:
			image_alt = os.path.splitext(os.path.basename(node['uri']))[0]
			image_alt = re.sub("[-_.]", " ", image_alt)
			node['alt'] = image_alt.capitalize()
		node['title'] = node['alt']
		node.known_attributes += ('title', )
		#import pdb; pdb.set_trace()
		print(node.attributes)

		return HTMLTranslator.visit_image(self, node)
	#def depart_image(self, node):
	#	import pdb; pdb.set_trace()


class Article(GenericContent):
	type = "articles"
	__indexes__ = [ArticlesIndex]
	__extensions__ = ["rst"]
	__slots__ = GenericContent.__slots__ + [
		"raw",
		"next",
		"title",
		"content",
		"excerpt",
		"previews",
		"metadata",
		"__weakref__",
		]

	def __init__(self, path, settings):
		super().__init__(path, settings)
		self.raw = None
		self.content = None
		self.metadata = None
		self.previews = None
		self.next = None
		self.log = logger.get_logger("Article", self.settings)

	def __getattr__(self, key):
		if key in self.metadata:
			return self.metadata[key]
		return super().__getattr__(key)

	@property
	def compilable(self):
		return True

	def compile(self):
		self.log.debug("Compiling '{}'".format(
			utils.get_better_path_rep(self.src_path)
			))
		extra_params = {
				'initial_header_level': '2',
				'syntax_highlight': 'short',
				'input_encoding': 'utf-8',
				'embed_stylesheet': False,
				'report_level': 5,
				'tab_width': 4,
				}
		self.raw = docutils.core.Publisher(
			destination_class=docutils.io.StringOutput
			)
		self.raw.set_components('standalone', 'restructuredtext', 'html')

		translator = partial(ArticleTranslator, article=self)
		self.raw.writer.translator_class = translator
		self.raw.process_programmatic_settings(None, extra_params, None)
		self.raw.set_source(source_path=self.src_path)
		self.raw._stderr = None
		out = self.raw.publish(enable_exit_status=False)
		for ln, lvl, msg in _process_system_messages(self.raw.document.parse_messages):
			msg = "{} ({}:{})".format(msg, self.norm_src_path, ln)
			if lvl == 1:
				self.log.info(msg)
			if lvl == 2:
				self.log.warn(msg)
			else:
				self.log.error(msg)

		self.metadata = _parse_metadata(self.raw, self.slug, self.settings)
		self.slug = self.metadata['slug']
		self.title = self.metadata['title']
		self.content = self.raw.writer.parts['body']
		self.excerpt = utils.truncate_html_words(self.content, 100)

	def deploy(self, site):
		site.theme.write(
			self,
			"article.html",
			env={
				'settings': self.settings,
				'site': site,
				'meta': self.metadata,
				'content': self,
				}
			)

		self.out_hash = utils.sha1(self.out_path)

	@property
	def cache_obj(self):
		meta = copy.deepcopy(self.metadata)
		out = super().cache_obj
		out['meta'] = meta
		out['content'] = base64.b64encode(bytes(self.content, 'utf-8'))
		return out

def _parse_metadata(pub, slug, settings):
	output = {
		'title': pub.writer.parts['title'],
		'subtitle': pub.writer.parts['subtitle'],
		"category": settings['site.default_category'],
		"author": settings['site.default_author'],
		"slug": slug,
		"date": None,
		"tags": None,
		"modified": None,
		"authors": None,
	}

	docinfo = pub.document.traverse(docutils.nodes.docinfo)[0]
	for element in docinfo.children:
		if element.tagname == 'field':
			name_elem, body_elem = element.children
			name = name_elem.astext()
			value = body_elem.astext()
		elif element.tagname == 'authors':
			name = element.tagname
			value = [element.astext() for element in element.children]
			value = ','.join(value)
		else:
			name = element.tagname
			value = element.astext()
		name = name.lower()

		output[name] = _process_metadata(name, value, settings)

	if output["authors"]:
		output["author"] = None

	if not (output["title"] and output["date"] and output["category"]):
		raise ex.ObligatoryFieldsException(
			"Article must have 'title', 'date' and 'category' set"
			)
	return output

def _process_metadata(name, value, settings):
	value = value.strip()
	if name == "authors" or name == "tags" or name == "category":
		sep = ">" if name == "category" else ","
		if sep not in value:
			value = value.strip()
		else:
			value = [val.strip()
						for val in value.split(sep) if val.strip()]
	elif name == "date" or name == "modified":
		fmt = settings['core.datetime_fmt']
		value = datetime.strptime(value, fmt)
	return value


def _process_system_messages(messages):
	if not messages:
		return []

	errors_by_line = {}
	for nessage in messages:
		line = nessage['line']
		level = nessage['level']
		text = nessage.children[0].astext().split('\n')[0].strip()
		if line in errors_by_line:
			if level > errors_by_line[line][1]:
				errors_by_line[line] = (line, level, text)
		else:
			errors_by_line[line] = (line, level, text)

	errors_by_message = {}
	for line, level, text in errors_by_line.values():
		if text in errors_by_message:
			errors_by_message[text].append((line, level, text))
			errors_by_message[text].sort(key=lambda x:x[0])
		else:
			errors_by_message[text] = [(line, level, text)]

	for errors in errors_by_message.values():
		lines = ', '.join(["L{}".format(error[0]) for error in errors])
		level = errors[0][1]
		message = errors[0][2]
		yield(lines, level, message)
