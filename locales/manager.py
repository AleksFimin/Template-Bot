from os import listdir
import json

path = 'locales/'
locales = listdir(path)
localization = {}

for locale in locales:
    if locale in ['manager.py', '__pycache__']:
        continue

    with open(f'{path}{locale}', 'r') as file:
        locale = locale.replace('.json', '')
        local_value = json.load(file)
        localization.update({locale: local_value})
              
if not localization:
    raise FileNotFoundError('locales not found')


def gettext(language, key):
    return localization[language][key]