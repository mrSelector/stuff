"""Створіть функцію, яка формує CSV-файл на основі даних, введених користувачем через консоль.
Файл має містити такі стовпчики: імена, прізвища, дати народження та місто проживання.
Реалізуйте можливості перезапису цього файлу, додавання нових рядків до наявного файлу,
рядкового читання з файлу та конвертації всього вмісту у формати та JSON."""
import csv
import json

def create_csv():
    data = []
    column = ['Name', 'Lastname', 'Birthday','City']
    name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    birthday = input("Введіть день народження: ")
    city = input("Введіть місто: ")
    data.append([name, last_name, birthday, city])

    with open("Users.csv",'w') as file:
        writer = csv.writer(file)
        writer.writerow(column)
        writer.writerows(data)

def apdate_csv():
    data = []
    name = input("Введіть ім'я: ")
    last_name = input("Введіть прізвище: ")
    birthday = input("Введіть день народження: ")
    city = input("Введіть місто: ")
    data.append([name, last_name, birthday, city])

    with open("Users.csv",'a') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def read_csv():
    with open('Users.csv','r')as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def json_convert():
    with open('Users.csv','r')as file:
        reader = csv.DictReader(file)
        data = list(reader)
        json_data = json.dumps(data)
        print(json_data)


def interface():
    while True:
        print('1. Створиті файл')
        print('2. Доповнити файл')
        print('3. Перезапис файла')
        print('4. Читання файла')
        print('5. Конвертування файлу у JSON')
        print('6. Exit')

        res = input('-->')
        if res == '1':
            create_csv()
        elif res == '2':
            apdate_csv()
        elif res == '3':
            create_csv()
        elif res == '4':
            read_csv()
        elif res == "5":
            json_convert()
        elif res == "6":
            break
        else:
            print('Ведіть номер дії')
            print(res)


if __name__ == '__main__':
    interface()