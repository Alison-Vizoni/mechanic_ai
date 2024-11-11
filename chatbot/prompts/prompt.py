from os import path


def get_prompt():
    directory = path.join('files', 'default_prompt.txt')
    with open(directory) as f:
        file = f.read()
    return file
