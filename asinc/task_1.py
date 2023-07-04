""""Створіть співпрограму, яка отримує контент із зазначених посилань і логує хід виконання в database,
 використовуючи стандартну бібліотеку requests, а потім проробіть те саме з бібліотекою aiohttp.
Кроки, які мають бути залоговані: початок запиту до адреси X, відповідь для адреси X отримано зі статусом 200.
Перевірте хід виконання програми на >3 ресурсах і перегляньте послідовність запису логів в обох варіантах
і порівняйте результати. Для двох видів завдань використовуйте різні файли для логування,
 щоби порівняти отриманий результат. """

import asyncio
import aiohttp
import sqlite3
import requests

# Підключення до бази даних
connection = sqlite3.connect('logs.db')

# Ресурси
SITES = [
    "http://www.testingmcafeesites.com/index.html",
    "https://www.jython.org",
    "http://www.gogle.com",
    "http://www.github.com",
    "http://www.itvdn.com"
]


def create_table_db(connect, name_table):
    """Функція створює таблицю БД"""

    cursor = connect.cursor()
    cursor.execute(f"""CREATE TABLE IF NOT EXISTS {name_table} (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    URL TEXT,
                    STATUS_CODE INTEGER)""")
    connect.commit()


def with_requests(connect, urls, name_table):
    """Функція яка логує запити за допомогою бібліотеки requests"""

    create_table_db(connect, name_table)
    for url in urls:
        response = requests.get(url)
        insert_logs(connect, name_table, url, response.status_code)


def insert_logs(connect, name_table, url, status_code):
    """Функція яка відправляє логи до БД"""

    cursor = connect.cursor()
    cursor.execute(f"INSERT INTO {name_table} (url, status_code) VALUES (?, ?)",
                   (url, status_code))
    connect.commit()


async def with_aiohttp(session, url, connect, name_table):
    """Функція логує запити за допомогою бібліотеки aiohttp"""

    async with session.get(url) as response:
        insert_logs(connect, name_table, url, response.status)


async def download_all_sites(connect, urls, name_table):
    """Співпрограма створює сеанс то створює таски для асинхронного виконання  """
    create_table_db(connect, name_table)
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(with_aiohttp(session, url, connect, name_table)) for url in urls
        ]
        await asyncio.gather(*tasks)
        connect.close()

if __name__ == '__main__':
    with_requests(connection, SITES, name_table='logs_requests')
    asyncio.run(download_all_sites(connection, SITES, 'logs_aiohttp'))
