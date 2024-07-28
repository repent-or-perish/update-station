#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
# from glob import glob
from setuptools import setup

# import DistUtilsExtra.command.build_extra
# import DistUtilsExtra.command.build_i18n
# import DistUtilsExtra.command.clean_i18n

# to update i18n .mo files (and merge .pot file into .po files) run on Linux:
# ,,python setup.py build_i18n -m''

for line in open('src/update-station').readlines():
    if line.startswith('__VERSION__'):
        exec(line.strip())
        break
# Silence flake8, __VERSION__ is properly assigned below
else:
    __VERSION__ = '5.1'

PROGRAM_VERSION = __VERSION__
prefix = sys.prefix

# compiling translations
os.system("sh src/compile_translations.sh")


def datafilelist(installbase, sourcebase):
    datafileList = []
    for root, subFolders, files in os.walk(sourcebase):
        fileList = []
        for f in files:
            fileList.append(os.path.join(root, f))
        datafileList.append((root.replace(sourcebase, installbase), fileList))
    return datafileList


data_files = [
    (f'{prefix}/etc/xdg/autostart', ['src/update-station.desktop']),
    (f'{prefix}/share/applications', ['src/update-manager.desktop']),
    (f'{prefix}/lib/update-station', ['src/need_reboot.json']),
    (f'{prefix}/etc/sudoers.d', ['src/sudoers.d/update-station']),
    (f'{prefix}/share/locale/ru/LC_MESSAGES', ['src/locale/ru/update-station.mo']),

]

data_files.extend(datafilelist(f'{prefix}/share/locale', 'build/mo'))

setup(
    name="update-station",
    version=PROGRAM_VERSION,
    description="Update Manager For GhostBSD/FreeBSD",
    license='BSD',
    author='Eric Turgeon',
    url='https://github/GhostBSD/update-station/',
    package_dir={'': 'src'},
    data_files=data_files,
    install_requires=['setuptools'],
    py_modules=['updateHandler', 'update_data'],
    scripts=['src/update-station']
)
