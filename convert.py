from shutil import which
import subprocess
import json
import os


def convert(arguments:dict):
    if not isinstance(arguments, dict):
        raise TypeError('"arguments" isn\'t a dictonary')
    if which('pandoc') is None: # checks if pandoc is installed
        raise FileExistsError('pandoc is not installed')
    

    arguments_list = ['pandoc', '-s', arguments['input_file'], '-o', arguments['output_file']]

    if arguments['toc']:
        arguments_list.append('--toc')

    subprocess.run(arguments_list)


