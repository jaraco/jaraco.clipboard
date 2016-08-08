from pyperclip import copy as copy_text, paste as paste_text

if copy_text.__name__ == 'ClipboardUnavailable':
	del copy_text
	del paste_text
