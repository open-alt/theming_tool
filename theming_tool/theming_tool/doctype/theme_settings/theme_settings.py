# -*- coding: utf-8 -*-
# Copyright (c) 2020, Ahmed Al-Farran and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document
import os
from os.path import join as join_path, exists

class ThemeSettings(Document):
	def validate(self):
		self.copy_image_file()
		self.copy_font_file()
		self.validate_theme()

	def validate_theme(self):
		'''Generate theme css if theme_scss has changed'''
		if self.theme_scss:
			doc_before_save = self.get_doc_before_save()
			if doc_before_save is None or self.theme_scss != doc_before_save.theme_scss:
				self.generate_bootstrap_theme()
		else:
			dir = frappe.utils.get_bench_path() + '/sites/assets/' + get_site_name() + '/theme/css'
			clear_font_folder_cmd = ('cd {0} && rm -rf custom_theme.css').format(dir)
			os.system(clear_font_folder_cmd)

	def generate_bootstrap_theme(self):
		dir = frappe.utils.get_bench_path() + '/sites/assets/' + get_site_name() + '/theme/css'
		is_dir_exists(dir)

		from subprocess import Popen, PIPE
		file_name = 'custom_theme.css'
		output_path = join_path(dir, file_name)
		content = self.theme_scss or ''
		content = content.replace('\n', '\\n')
		command = ['node', 'generate_bootstrap_theme.js', output_path, content]
		process = Popen(command, cwd=frappe.get_app_path('frappe', '..'), stdout=PIPE, stderr=PIPE)
		self.bench_build()
		frappe.msgprint(_('Compiled Successfully'), alert=True)

	def copy_font_file(self):
		dir = frappe.utils.get_bench_path() + '/sites/assets/' + get_site_name() + '/theme/font'
		is_dir_exists(dir)
		if self.font:
			doc_before_save = self.get_doc_before_save()
			if doc_before_save is None or self.font != doc_before_save.font:
				site_name = get_site_name()
				if os.path.dirname(self.font_path) == "/files":
					font_path = "/public" + self.font_path
				else :
					font_path = self.font_path

				font_file = "'" + frappe.utils.get_bench_path() + "/sites/" + site_name + font_path + "'"
				clear_font_folder_cmd = ('cd {0} && rm *').format(dir)
				os.system(clear_font_folder_cmd)
				copy_font_file_cmd = ('cp {0} {1}').format(font_file, dir)
				os.system(copy_font_file_cmd)
		if not self.font:
			clear_font_folder_cmd = ('cd {0} && rm *').format(dir)
			os.system(clear_font_folder_cmd)

	def copy_image_file(self):
		dir = frappe.utils.get_bench_path() + '/sites/assets/' + get_site_name() + '/theme/images'
		is_dir_exists(dir)
		if self.logo:
			doc_before_save = self.get_doc_before_save()
			if doc_before_save is None or self.logo != doc_before_save.logo:
				site_name = get_site_name()
				if os.path.dirname(self.logo) == "/files":
					logo = "/public" + self.logo
				else :
					logo = self.logo

				image_file = "'" + frappe.utils.get_bench_path() + "/sites/" + site_name + logo + "'"
				clear_image_folder_cmd = ('cd {0} && rm *').format(dir)
				os.system(clear_image_folder_cmd)
				copy_image_file_cmd = ('cp {0} {1}').format(image_file, dir)
				os.system(copy_image_file_cmd)
		if not self.logo:
			clear_image_folder_cmd = ('cd {0} && rm *').format(dir)
			os.system(clear_image_folder_cmd)

	def bench_build(self):
		command = ('cd {0} && bench build --app theming_tool').format(frappe.utils.get_bench_path())
		os.system(command)

def is_dir_exists(dir):
	if not os.path.exists(dir):
		os.makedirs(dir)

@frappe.whitelist()
def get_site_name():
	return frappe.local.site_path.strip("./")
