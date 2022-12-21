from shutil import which


def convert():
    if which('pandoc') is None: # checks if pandoc is installed
        raise FileExistsError('pandoc is not installed')

    

if __name__ == "__main__":
    pass