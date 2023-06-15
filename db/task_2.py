"""Створіть консольний інтерфейс (CLI) на Python для додавання нових записів до бази даних."""
import sqlite3

connection = sqlite3.connect('expenses.db')


def create_table(connect):
    cursor = connect.cursor()
    cursor.execute("""CREATE table expenses 
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      Purpose varchar(15),
                      Amount REAL,
                      Time varchar(10))
                      """)
    connect.commit()


def input_data():
    purpose = input('Введіть призначення витрат: ')
    amount = input('Введіть суму витрат: ')
    time = input('Введіть час витрат: ')
    data = {
        "purpose": purpose,
        "amount": amount,
        "time": time
    }
    return data


def insert_data(connect, data):
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO expenses (Purpose, Amount, Time) VALUES (?,?,?);""",
                   (data["purpose"], data["amount"], data["time"]))
    connect.commit()


create_table(connection)
while True:
    user_data = input_data()
    insert_data(connection, user_data)
    res = input('Введіть "exit" для завешення: ')
    if res == 'exit':
        break


connection.close()
