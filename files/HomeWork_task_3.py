"""Задание 3
Модифицируйте исходный код сервиса по сокращению ссылок из предыдущих двух уроков так, чтобы
он сохранял базу ссылок на диске и не «забывал» при перезапуске. При желании можете ознакомиться
с модулем shelve (https://docs.python.org/3/library/shelve.html), который в данном случае будет весьма
удобен и упростит выполнение задания."""
from HomeWork_task_3_2 import DataBase


def add_url():
    while True:
        name_url = input('Enter name URL: ')
        full_url = input('Enter full URL: ')
        try:
            db.add_link(name_url, full_url)
        except (KeyError, ValueError) as error:
            print(error)
        else:
            break


def get_link():
    name_url = input('Enter name URL: ')
    url = db.get_link(name_url)
    print(url)


def interface():
    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')
        res = input('-->')
        if res == '1':
            add_url()
        elif res == '2':
            get_link()
        elif res == '3':
            break
        else:
            print('Enter your choice')


if __name__ == '__main__':
    db = DataBase()
    interface()
