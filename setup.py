#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import itertools

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

# richxerox has invalid versions in PyPI, so exclude them
# https://bitbucket.org/jeunice/richxerox/issues/2
bad_versions = itertools.chain(range(1,12), [127, 128])
bad_version_specs = map('!=0.{0:02d}'.format, bad_versions)
richxerox = 'richxerox' + ','.join(bad_version_specs)

name = 'jaraco.clipboard'
description = 'Multi-format, cross-platform clipboard library'

params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	install_requires=[
	],
	extras_require={
		':sys_platform=="win32"': 'jaraco.windows>=3.4',
		':sys_platform=="darwin"': richxerox,
		':sys_platform=="linux2" or sys_platform=="linux"': "pyperclip",
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
