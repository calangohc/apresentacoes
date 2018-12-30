#!/usr/bin/env python
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
from jinja2 import Environment
from jinja2 import FileSystemLoader

import folios
from folios.core import logger
from folios.core import utils


class Theme(object):
    def __init__(self, settings):
        self.settings = settings
        self.log = logger.get_logger("Theme", self.settings)

        self.theme_name = settings['site.theme']
        sitepath = utils.resolve_root_folder()
        if self.theme_name == 'default':
            self.basepath = os.path.join(folios.__root__, 'data', 'themes', 'default')
        else:
            self.basepath = os.path.join(sitepath, self.theme_name)
        self.templates_path = os.path.join(self.basepath, 'templates')
        self.static_path = os.path.join(self.basepath, 'static')

        if not os.path.exists(self.templates_path):
            raise ex.UnexistentSourceException(
                "Couldn't find theme '{}' at '{}'".format(self.theme_name,
                    self.templates_path)
                )

        self.env = Environment(
            trim_blocks=True,
            lstrip_blocks=True,
            loader=FileSystemLoader(self.templates_path),
        )

    @property
    def templates(self):
        return (template for template in self.env.list_templates())

    @property
    def compilable(self):
        return False

    def compile(self):
        raise NotImplemented

	def deploy(self, site):
		self.log.info("Deploying theme '{}'".format(self.theme_name))
		if not os.path.exists(self.static_path):
			return

		root, folders, files = os.walk(self.static_path).__next__()
		for folder in folders:
			src_path = os.path.join(self.static_path, folder)
			out_path = os.path.join(
				self.settings.get_path('core.output'),
				folder
				)
			self.log.debug("Deploying '{}' to '{}'".format(
				folder, out_path
				))
			utils.copy(src_path, out_path)

	def write(self, content, template_name, env):
		self.log.debug("Writing '{}' for '{}'".format(
			content.slug,
			utils.get_better_path_rep(content.out_path),
			))
		template = self.env.get_template(template_name)
		output = template.render(**env)

		utils.mkdir(os.path.dirname(content.out_path))
		with open(content.out_path, 'w', encoding='utf-8') as f:
			f.write(output)
