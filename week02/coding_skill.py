import json
import sys


filename = sys.argv[1]


with open(filename) as f:
    data = json.load(f)

languages = {}
for person in data['people']:
    name_person = "{} {}".format(person["first_name"], person["last_name"])
    for lang in person['skills']:
        language = lang['name']
        level = lang['level']
        if language in languages:
            if languages[language]['level'] > level:
                continue
        languages[language] = {"name": name_person, "level": level}

for l in languages:
    print("{} - {}".format(l, languages[l]['name']))
