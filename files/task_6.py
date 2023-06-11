"""Для таблиці «матеріалу» з завдання 4 створіть функцію користувача,
 яка приймає необмежену кількість полів і повертає їх конкатенацію."""

import sqlite3
import json


def concatenate_fields(*args):
    string_args = [str(arg) for arg in args]
    return " ".join(string_args)


def adapt_json(list_data):
    return json.dumps(list_data).encode('utf-8')


def convert_json(raw):
    return json.loads(raw)


sqlite3.register_adapter(list, adapt_json)
sqlite3.register_converter('json', convert_json)
connect = sqlite3.connect('data/materials.db', detect_types=sqlite3.PARSE_DECLTYPES)
#connect = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()
connect.create_function("concatenate", -1, concatenate_fields)


cursor.execute(""" CREATE TABLE materials
                    (id INTEGER PRIMARY KEY,
                     weight REAL,
                     height REAL,
                     additional_info TEXT
                     );""")

cursor.execute("""INSERT INTO materials VALUES (?,?,?,?)""",
               (1, 234, 453, [('color', 'white'), ('steel', 'titan')]))
cursor.execute("""INSERT INTO materials (weight, height, additional_info) VALUES(?, ?, ?)""",
               (5574, 4287, [('color', 'red'), ('wood', 'pine')]))

connect.commit()
fields = cursor.execute("SELECT concatenate(id, weight, height, additional_info) FROM materials")
print(fields.fetchall())
# for field in fields.fetchall():
#     print(*field)
