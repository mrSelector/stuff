"""Зробіть таблицю для підрахунку особистих витрат із такими полями: id, призначення, сума, час."""

import sqlite3

connect = sqlite3.connect('expenses.db')
cursor = connect.cursor()
cursor.execute("""CREATE table expenses 
                  (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                  Purpose varchar(15),
                  Amount REAL,
                  Time varchar(10))
                  """)
connect.commit()
connect.close()
