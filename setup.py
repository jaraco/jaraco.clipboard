#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io
import sys
import itertools

import setuptools

with io.open('README.rst', encoding='utf-8') as readme:
	long_description = readme.read()

needs_pytest = {'pytest', 'test'}.intersection(sys.argv)
pytest_runner = ['pytest_runner'] if needs_pytest else []
needs_sphinx = {'release', 'build_sphinx', 'upload_docs'}.intersection(sys.argv)
sphinx = ['sphinx', 'rst.linker'] if needs_sphinx else []
needs_wheel = {'release', 'bdist_wheel'}.intersection(sys.argv)
wheel = ['wheel'] if needs_wheel else []

# richxerox has invalid versions in PyPI, so exclude them
# https://bitbucket.org/jeunice/richxerox/issues/2
bad_versions = itertools.chain(range(1,12), [127, 128])
bad_version_specs = map('!=0.{0:02d}'.format, bad_versions)
richxerox = 'richxerox' + ','.join(bad_version_specs)

name = 'jaraco.clipboard'
description = 'Multi-format, cross-platform clipboard library'

setup_params = dict(
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
		'setuptools_scm>=1.9',
	] + pytest_runner + sphinx + wheel,
	tests_require=[
		'pytest>=2.8',
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
	setuptools.setup(**setup_params)
