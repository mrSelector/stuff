"""Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу.
Поле «додаткові  характеристики матеріалу» має зберігати у собі масив,
кожен елемент якого є кортежем із двох значень: перше – назва характеристики, а друге – її значення."""
import sqlite3
import json


def adapt_json(list_data):
    return json.dumps(list_data)


def convert_json(raw):
    return json.loads(raw)


sqlite3.register_adapter(list, adapt_json)
sqlite3.register_converter('json', convert_json)
connect = sqlite3.connect('data/materials.db', detect_types=sqlite3.PARSE_DECLTYPES)
# connect = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE materials
                    (id INTEGER PRIMARY KEY,
                     weight REAL,
                     height REAL,
                     additional_info TEXT
                     );""")

cursor.execute("""INSERT INTO materials VALUES (?,?,?,?)""",
               (1, 234, 453, [('color', 'white'), ('steel', 'titan')]))

connect.commit()
data = cursor.execute('SELECT * FROM "materials"').fetchall()
print(data)
