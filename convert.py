from shutil import which
import subprocess
import json
import os


def convert(arguments:dict):
    if not isinstance(arguments, dict):
        raise TypeError('"arguments" isn\'t a dictonary')
    if which('pandoc') is None: # checks if pandoc is installed
        raise FileExistsError('pandoc is not installed')
    

    arguments = ['pandoc', '-s', arguments['input_file'], '-o', arguments['output_file']]
    subprocess.run(arguments)


