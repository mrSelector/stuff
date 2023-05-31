"""Задание 2
Создайте таблицу «материалы» из следующих полей: идентификатор, вес, высота и доп.
характеристики материала. Поле доп. характеристики материала должно хранить в себе массив,
каждый элемент которого является кортежем из двух значений, первое – название
характеристики, а второе – её значение"""
import sqlite3
import json

connect = sqlite3.connect('data/materials.db')

connect.execute(""" CREATE TABLE "materials"
                    (id INTEGER PRIMARY KEY,
                     weight REAL,
                     height REAL,
                     additional_info TEXT
                     )""")

mat = {'id': 1, 'weight': 72, 'height': 186, 'add': [('color', 'white')]}
json_data = json.dumps(mat.get('add', 'empty'))
# connect.execute("INSERT INTO materials VALUES (?,?,?,?)", (mat['id'], mat['weight'], mat['height'], json_data))
connect.execute("INSERT INTO materials VALUES (1, 33, 444, 'test'")
# data = connect.execute('SELECT * FROM "materials"').fetchall()
# print(data)