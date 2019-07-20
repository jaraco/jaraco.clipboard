import pyperclip

copy_text, paste_text = pyperclip.determine_clipboard()

unavailable = any(
    isinstance(func, object) and type(func).__name__ == 'ClipboardUnavailable'
    for func in locals().values()
)

if unavailable:
    del copy_text
    del paste_text
