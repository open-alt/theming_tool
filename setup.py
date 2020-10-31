# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in theming_tool/__init__.py
from theming_tool import __version__ as version

setup(
	name='theming_tool',
	version=version,
	description='Theming tool for frappe',
	author='Ahmed Al-Farran',
	author_email='afarran1992@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
