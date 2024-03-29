"""Створіть таблицю «матеріали» з таких полів: ідентифікатор, вага, висота та додаткові характеристики матеріалу.
Поле «додаткові  характеристики матеріалу» має зберігати у собі масив,
кожен елемент якого є кортежем із двох значень: перше – назва характеристики, а друге – її значення."""
import sqlite3
import json

connect = sqlite3.connect('data/materials.db')
#connect = sqlite3.connect(':memory:')

connect.execute(""" CREATE TABLE "materials"
                    (id INTEGER PRIMARY KEY,
                     weight REAL,
                     height REAL,
                     additional_info TEXT
                     )""")

mat = {'id': 1, 'weight': 72, 'height': 186, 'add': [('color', 'white'), ('steel', 'titan')]}
json_data = json.dumps(mat.get('add', 'empty'))
connect.execute("""INSERT INTO materials VALUES (?,?,?,?)""", (1, mat['weight'], mat['height'], json_data))

connect.commit()
data = connect.execute('SELECT * FROM "materials"').fetchall()
print(data)

