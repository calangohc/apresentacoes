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

'''
Nem sempre faço o que é melhor pra mim,
mas nunca faço o que eu não tô afim de fazer.

Não quero perder a razão pra ganhar a vida.
Nem perder a vida pra ganhar o pão.
Não é que eu faça questão de ser feliz,
eu só queria que parassem de morrer de fome a um palmo do meu nariz.
Mesmo que pareçam bobagens as viagens que eu faço,
eu traço meus rumos eu mesmo (a esmo).

        --- Nunca se Sabe (Engenheiros do Hawaii)
'''

import os

from subprocess import call
from PIL import Image as PILImage

from folios.core import utils
from folios.core import logger
from folios.core.contents import GenericContent
from folios.core import exceptions as ex

# JPEGTRANS: gallery2-jpegtran
# OPTIPNG: optipng

OPTIMIZERS = {
    'jpg': 'jpegtran -copy none -optimize -outfile "{output}" "{input}"',
    'png': 'optipng "{input}" -out "{output}"',
    }


class Image(GenericContent):
	type = "images"
	__extensions__ = ("jp", "jpg", "jpeg", "png", "gif", "bmp", "svg")
	__slots__ = GenericContent.__slots__ + [
		'size'
		]

	def __init__(self, path, settings):
		super().__init__(path, settings)
		self.log = logger.get_logger("Image", settings)
		self.size = (None, None)
		with PILImage.open(self.src_path) as _img:
			self.size = _img.size

	@property
	def compilable(self):
		return self.extension.lower() in {'jp', 'jpg', 'jpeg', 'png'}

	def compile(self):
		pass

	def deploy(self, site=None):
		if self.extension.lower() in {'jp', 'jpg', 'jpeg'}:
			command = OPTIMIZERS['jpg']
		elif self.extension.lower() == 'png':
			command = OPTIMIZERS['png']
		else:
			self.log.debug("Deploying '{}' for '{}'".format(
				utils.get_better_path_rep(self.src_path),
				utils.get_better_path_rep(self.out_path),
				))
			utils.copy(self.src_path, self.out_path)
			return

		utils.mkdir(os.path.dirname(self.out_path))
		command = command.format(input=self.src_path, output=self.out_path)
		self.log.debug("Optimizing '{}' for '{}'".format(
			utils.get_better_path_rep(self.src_path),
			utils.get_better_path_rep(self.out_path),
			))
		retcode = call(command, shell=True)
		if retcode != 0:
			cmd = command.split()[0]
			raise ex.ContentCompilingException(
				"Error while optimizing image '{}'. Please ensure you have "
				"{} installed".format(self.norm_src_path, cmd)
				)
		self.out_hash = utils.sha1(self.out_path)

    @property
    def cache_obj(self):
        out = super().cache_obj
        out['size'] = self.size
        return out
