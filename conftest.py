import platform

platform_names = 'Linux', 'Darwin', 'Windows'

collect_ignore = [
    'jaraco/clipboard/{name}.py'.format(**locals())
    for name in platform_names
    if platform.system() != name
]
