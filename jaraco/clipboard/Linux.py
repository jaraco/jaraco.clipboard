from pyperclip import copy as copy_text, paste as paste_text

unavailable = any(
	isinstance(func, object)
	and type(func).__name__ == 'ClipboardUnavailable'
	for func in locals().values()
)

if unavailable:
	del copy_text
	del paste_text
