import platform

platform_names = 'Linux', 'Darwin', 'Windows'

collect_ignore = [
    f'jaraco/clipboard/{name}.py'
    for name in platform_names
    if platform.system() != name
]
