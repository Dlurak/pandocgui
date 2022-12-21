from shutil import which
import subprocess
import json
import os
import pathlib

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file_extensions.json'), 'r') as json_file: # write the content of the config to the var config
    file_extensions = json.load(json_file)

def convert(arguments:dict):
    input_file_extension = pathlib.Path(arguments['input_file']).suffix
    output_file_extension = pathlib.Path(arguments['output_file']).suffix

    if not isinstance(arguments, dict):
        raise TypeError('"arguments" isn\'t a dictonary')
    if which('pandoc') is None: # checks if pandoc is installed
        raise FileExistsError('pandoc is not installed')
    if not (input_file_extension in file_extensions.keys()):
        raise KeyError(f'Either Pandoc or this programm doesn\'t support the file extension {input_file_extension}')
    if not (output_file_extension in file_extensions.keys()):
        raise KeyError(f'Either Pandoc or this programm doesn\'t support the file extension {output_file_extension}')

    arguments = ['pandoc', '-s', arguments['input_file'], '-f', file_extensions[input_file_extension], '-t', file_extensions[output_file_extension], '-o', arguments['output_file']]
    subprocess.run(arguments)


