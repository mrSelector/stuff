"""Створіть агрегатні функції для підрахунку загальної кількості  витрат i прибуткiв за місяць.
 Забезпечте відповідний інтерфейс користувача."""

import sqlite3

connection = sqlite3.connect('expenses.db')


def create_table(connect):
    cursor = connect.cursor()
    cursor.execute("""CREATE table expenses 
                      (ID INTEGER PRIMARY KEY AUTOINCREMENT,
                      Purpose varchar(15),
                      Amount REAL,
                      Income REAL,
                      Time varchar(10))
                      """)
    connect.commit()
    connect.close()


class Total:
    def __init__(self):
        self.numbers = set()

    def step(self, number):
        self.numbers.add(number)

    def finalize(self):
        return sum(self.numbers)


def input_data_expenses():
    purpose = input('Введіть призначення витрат: ')
    amount = input('Введіть суму витрат: ')
    time = input('Введіть час витрат: ')
    data = {
        "purpose": purpose,
        "amount": amount,
        "time": time
    }
    return data


def input_data_income():
    income = input('Введіть ваш прибуток: ')
    time = input('Введіть час: ')
    purpose = input('Введіть походження прибутку: ')
    data = {
        "income": income,
        "time": time,
        "purpose": purpose
    }
    return data


def insert_data_expenses(connect, data):
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO expenses (Purpose, Amount, Time) VALUES (?,?,?);""",
                   (data["purpose"], data["amount"], data["time"]))
    connect.commit()


def insert_data_income(connect, data):
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO expenses(Purpose, Income, Time) VALUES (?,?,?);""",
                   (data["purpose"], data["income"], data["time"]))
    connect.commit()


def total_expenses(connect):
    cursor = connect.cursor()
    cursor.execute("""SELECT total(Income) AS result FROM expenses""")
    return cursor.fetchall()[0]


def total_income(connect):
    cursor = connect.cursor()
    cursor.execute("""SELECT total(Amount) AS result FROM expenses""")
    return cursor.fetchall()[0]


create_table(connection)

while True:
    print("1.Внесення витрат")
    print("2.Внесення прибутка")
    print("3.Загальна сума витрат")
    print("4.Загальна сума прибутків")
    print("Для виходу введіть 'exit'")
    choice = input("--->")
    if choice == '1':
        user_data = input_data_expenses()
        insert_data_expenses(connection, user_data)
    elif choice == '2':
        user_data = input_data_income()
        insert_data_income(connection, user_data)
    elif choice == '3':
        print(f'Загальна сума витрат --> {total_expenses(connection)}')
    elif choice == '4':
        print(f'Загальна сума прибутків --> {total_income(connection)}')
    elif choice == 'exit':
        break

connection.close()
