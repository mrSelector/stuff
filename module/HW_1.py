"""Задание 1
Перепишите домашнее задание предыдущего урока (сервис для сокращения ссылок) таким образом,
чтобы у него была основная часть, которая отвечала бы за логику работы и предоставляла обобщённый
интерфейс, и модуль представления, который отвечал бы за взаимодействие с пользователем. При
замене последнего на другой, взаимодействующий с пользователем иным способом, программа
должна продолжать корректно работать."""

from HW_2 import DataBase


def add_link(db):
    name_url = input("Enter name for URL: ")
    url = input('Enter full URL: ')
    try:
        db.set_db(name_url, url)
    except (KeyError, ValueError) as error:
        print(error)


def get_link(db):
    name_url = input("Enter name for URL: ")
    res = db.get_db(name_url)
    print(res)


def interface():
    db = DataBase()
    while True:
        print('1. Add link')
        print('2. Get link')
        print('3. Exit')
        result = (input('-->'))
        if result == "1":
            add_link(db)
        elif result == "2":
            get_link(db)
        elif result == "3":
            break
        else:
            print('Enter some')


if __name__ == '__main__':
    interface()
