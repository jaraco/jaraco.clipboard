#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import setuptools

name = 'jaraco.clipboard'
description = 'Multi-format, cross-platform clipboard library'
nspkg_technique = 'managed'
"""
Does this package use "native" namespace packages or
pkg_resources "managed" namespace packages?
"""

name = 'jaraco.clipboard'
description = 'Multi-format, cross-platform clipboard library'

params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=(
		name.split('.')[:-1] if nspkg_technique == 'managed'
		else []
	),
	python_requires='>=2.7',
	install_requires=[
	],
	extras_require={
		'testing': [
			# upstream
			'pytest>=3.5,!=3.7.3',
			'pytest-sugar>=0.9.1',
			'collective.checkdocs',
			'pytest-flake8',

			# local
		],
		'docs': [
			# upstream
			'sphinx',
			'jaraco.packaging>=3.2',
			'rst.linker>=1.9',

			# local
		],
		':sys_platform=="win32"': [
			'jaraco.windows>=3.4',
		],
		':sys_platform=="darwin"': [
			'richxerox>=1.0.1',
		],
		':sys_platform=="linux2" or sys_platform=="linux"': [
			"pyperclip>=1.6",
		],
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
	],
	entry_points={
	},
)
if __name__ == '__main__':
	setuptools.setup(**params)
