import sys
from cx_Freeze import setup, Executable

base = None

executables = [
    Executable('mtaobao.py', base=base)
]

setup (
name = "mtaobao",
version = "2.0",
description = "hunterhug",
executables=executables
)
