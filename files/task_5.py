"""Для таблиці «матеріалу» з завдання 4 створіть користувальницьку агрегатну функцію,
 яка рахує середнє значення ваги всіх матеріалів вислідної вибірки й округляє значення до цілого. """
import sqlite3
import json


class Avg:

    def __init__(self):
        self.numbers = set()

    def step(self, number):
        self.numbers.add(number)

    def finalize(self):
        if self.numbers == 0:
            return 0
        return sum(self.numbers) / len(self.numbers)


def adapt_json(list_data):
    return json.dumps(list_data)


def convert_json(raw):
    return json.loads(raw)


sqlite3.register_adapter(list, adapt_json)
sqlite3.register_converter('json', convert_json)
connect = sqlite3.connect('data/materials.db', detect_types=sqlite3.PARSE_DECLTYPES)
#connect = sqlite3.connect(':memory:', detect_types=sqlite3.PARSE_DECLTYPES)
cursor = connect.cursor()

cursor.execute(""" CREATE TABLE materials
                    (id INTEGER PRIMARY KEY AUTOINCREMENT,
                     weight REAL,
                     height REAL,
                     additional_info TEXT
                     );""")

cursor.execute("""INSERT INTO materials (weight, height, additional_info) VALUES(?, ?, ?)""",
               (234, 453, [('color', 'white'), ('steel', 'titan')]))
cursor.execute("""INSERT INTO materials (weight, height, additional_info) VALUES(?, ?, ?)""",
               (5574, 4287, [('color', 'red'), ('wood', 'pine')]))

connect.commit()
cursor.execute('SELECT avg(weight) AS result FROM materials')
# cursor.execute('SELECT * FROM materials')
value = cursor.fetchall()[0]
print(int(value[0]))
