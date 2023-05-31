"""Задание 1
Создайте простые словари и сконвертируйте их в JSON. Сохраните JSON в файл и попробуйте
загрузить данные из файла"""

import json

dct1 = {'Olga': "dupka",
        'Pashko': "stereo",
        'Car': 'Honda'
        }
dct2 = {'Dog': "Ice",
        'work': "python",
        'hobby': 'event'
        }
data = dct1, dct2

with open('stuff.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('stuff.json', 'r') as f:
    con = json.load(f)
    print(con)
