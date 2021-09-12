import os, sys
from cx_Freeze import setup, Executable

setup(
    name = "pyDownloadManager",
    version = "1.0",
    description = "Free multithreaded modern download manager",
    author = "magnusjwatson2786",
    options = {'build_exe' : {'include_files' : ['terminal.ico','themes/']}},
    executables = [Executable(
    script="xt.py",
    base="Win32GUI",
    icon="terminal.ico")
    ] 
)