import jaraco.windows.clipboard as wclip

copy_text = wclip.set_unicode_text
paste_text = wclip.get_unicode_text

copy_html = wclip.set_html

def paste_html():
	wclip.get_html().html

paste_image = wclip.get_image
