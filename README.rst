.. image:: https://img.shields.io/pypi/v/jaraco.clipboard.svg
   :target: https://pypi.io/project/jaraco.clipboard

.. image:: https://img.shields.io/pypi/pyversions/jaraco.clipboard.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.clipboard/master.svg
   :target: https://travis-ci.org/jaraco/jaraco.clipboard

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: Black

.. image:: https://img.shields.io/appveyor/ci/jaraco/jaraco-clipboard/master.svg
   :target: https://ci.appveyor.com/project/jaraco/jaraco-clipboard/branch/master

.. image:: https://readthedocs.org/projects/jaracoclipboard/badge/?version=latest
   :target: https://jaracoclipboard.readthedocs.io/en/latest/?badge=latest

The only clipboard library for Python that supports text on all
three major platforms plus HTML on MacOS and HTML and images
on Windows.

Similar to `pyperclip <https://pypi.python.org/pypi/pyperclip/>`_
and `clipboard <https://pypi.python.org/pypi/clipboard/>`_
and `xerox <https://pypi.python.org/pypi/xerox/>`_ except attempts
to support more formats than just text.

This library is just a thin wrapper around the best platform implementations:

 - pyperclip for Linux
 - richxerox for MacOS
 - jaraco.windows for Windows

Usage
=====

``jaraco.clipboard`` supplies several functions in the clipboard module.
The most common are the copy and paste functions::

    from jaraco import clipboard
    clipboard.copy('some text')
    clipboard.paste() == 'some text'

Other functions include ``copy/paste`` ``html`` and ``image``.

If not implemented on your platform, the functions will raise
NotImplementedError.
