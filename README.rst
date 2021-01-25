.. image:: https://img.shields.io/pypi/v/jaraco.clipboard.svg
   :target: `PyPI link`_

.. image:: https://img.shields.io/pypi/pyversions/jaraco.clipboard.svg
   :target: `PyPI link`_

.. _PyPI link: https://pypi.org/project/jaraco.clipboard

.. image:: https://github.com/jaraco/jaraco.clipboard/workflows/tests/badge.svg
   :target: https://github.com/jaraco/jaraco.clipboard/actions?query=workflow%3A%22tests%22
   :alt: tests

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Code style: Black

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
The most common are the copy and paste functions:

.. code-block:: python

    from jaraco import clipboard
    clipboard.copy('some text')
    clipboard.paste() == 'some text'

Other functions include ``copy/paste`` ``html`` and ``image``.

If not implemented on your platform, the functions will raise
NotImplementedError.
