import functools

import richxerox

paste_text = richxerox.paste
copy_text = richxerox.copy

paste_html = functools.partial(richxerox.paste, format='html')
copy_html = functools.partial(richxerox.copy, format='html')
