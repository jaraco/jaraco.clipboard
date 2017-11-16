import pytest

from jaraco import clipboard


def needs_command(name):
	cmd = vars(clipboard)[name]

	return pytest.mark.xfail(
		cmd is clipboard._not_implemented,
		reason="{name} not implemented on this platform",
	)


@needs_command("copy_text")
def test_copy_text():
	clipboard.copy_text("foo")


@needs_command("paste_text")
def test_paste_text():
	# first ensure there's something on the clipboard:
	clipboard.copy_text('test for paste')
	assert clipboard.paste_text() == 'test for paste'
