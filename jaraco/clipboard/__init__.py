import platform
import importlib
import itertools


def _not_implemented(*args, **kwargs):
    raise NotImplementedError("format not supported")


def _init():
    _platform_mod_name = '.' + platform.system()
    _platform_mod = importlib.import_module(_platform_mod_name, 'jaraco.clipboard')

    # support copy and paste of text, html, and image.
    _modes = 'copy', 'paste'
    _formats = 'text', 'html', 'image'
    _methods = map('_'.join, itertools.product(_modes, _formats))

    for name in _methods:
        func = getattr(_platform_mod, name, _not_implemented)
        globals().update({name: func})

    globals().update(copy=globals()['copy_text'])
    globals().update(paste=globals()['paste_text'])


_init()


__all__ = [
    name
    for name, func in globals().items()
    if callable(func) and not name.startswith('_')
]
