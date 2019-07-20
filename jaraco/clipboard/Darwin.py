import functools

import richxerox

paste_text = richxerox.paste
copy_text = richxerox.copy

paste_html = functools.partial(richxerox.paste, format='html')


def copy_html(content):
    return richxerox.copy(html=content)
