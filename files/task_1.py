"""Створіть прості словники та конвертуйте їх у JSON. Збережіть JSON у файлі та спробуйте завантажити дані з файлу."""

import json

data = ({
            'car_brand': 'Honda',
            'model': 'Accord_euroR',
            'year': 2004,
            'engine': 2.0,
            'power': '220hp',
        },
        {
            'car_brand': 'Honda',
            'model': 'integra_TypeR',
            'year': 1997,
            'engine': 1.8,
            'power': '200hp',
        })
# json_data = json.dumps(data)
# print(json_data)


with open('Honda.json', 'w') as file:
    json.dump(data, file, indent=2)

with open('Honda.json', 'r') as file:
    result = json.load(file)
    print(result)
