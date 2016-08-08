jaraco.clipboard
================

.. image:: https://img.shields.io/pypi/v/jaraco.clipboard.svg
   :target: https://pypi.io/project/jaraco.clipboard

.. image:: https://img.shields.io/pypi/pyversions/jaraco.clipboard.svg

.. image:: https://img.shields.io/pypi/dm/jaraco.clipboard.svg

.. image:: https://img.shields.io/travis/jaraco/jaraco.clipboard/master.svg
   :target: http://travis-ci.org/jaraco/jaraco.clipboard

A thin wrapper around platform-specific implementations of clipboard
functionality.

Similar to `pyperclip <https://pypi.python.org/pypi/pyperclip/>`_
and `clipboard <https://pypi.python.org/pypi/clipboard/>`_
and `xerox <https://pypi.python.org/pypi/xerox/>`_ except attempts
to support more formats than just text.

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
