#!/usr/local/bin/python

import os
import sys

from utils import file_extension, file_name, file_extensions
from models import CodeFile

def get_code(path):
    name = file_name(path)
    extension = file_extension(name)
    if extension in file_extensions:
        return CodeFile(path, name, extension)
    return None

def traverse_dir(target):
    code_files = []
    for path, names, files in os.walk(target):
        for file in files:
            code = get_code(os.path.join(path, file))
            if code is not None:
                code_files.append(code)
    return code_files

if len(sys.argv) == 2:
    codes = traverse_dir(sys.argv[1])
    for code in codes:
        print code
