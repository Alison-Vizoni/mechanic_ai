from os import path

from config import settings


def get_prompt():
    directory = path.join(settings.BASE_DIR, 'chatbot', 'prompts', 'files', 'default_prompt.txt')
    with open(directory) as f:
        file = f.read()
    return file
