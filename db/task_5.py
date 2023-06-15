"""Create an Exchange Rates To USD db using API Monobank (api.monobank.ua).
Do requests via request lib, parse results, write it into db. (3 examples required)
Example:
Table - Exchange Rate To USD:

id (INT PRIMARY KEY) - 1, 2, 3, ...
currency_name (TEXT) - UAH
currency_value (REAL) - 39.5
current_date (DATETIME) - 10/22/2022 7:00 PM"""
import sqlite3
import requests
import datetime

connection = sqlite3.connect('Exchange_Rate.db')


def create_table(connect):
    cursor = connect.cursor()
    cursor.execute("""CREATE TABLE exchange_rate_to_USD (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    currency_name TEXT,
                    currency_value REAL,
                    current_date DATETIME)
                    """)
    connect.commit()


def response_data():
    response = requests.get('https://api.monobank.ua/bank/currency')
    return response.json()[0]


def insert_data(connect, data):
    cursor = connect.cursor()
    cursor.execute("""INSERT INTO exchange_rate_to_USD (currency_name, currency_value, current_date) VALUES (?,?,?)""",
                   ("USD - UAH", data.get('rateSell'), datetime.datetime.now()))
    connect.commit()


create_table(connection)
exchange = response_data()
insert_data(connection, exchange)
connection.close()
