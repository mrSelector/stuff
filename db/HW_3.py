"""Задание 3
Поработайте с созданием собственных диалектов, произвольно выбирая правила для CSV файлов.
Зарегистрируйте созданные диалекты и поработайте, используя их, с созданием/чтением файлом"""

import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "|"
    delimiter = "*"
    lineterminator = "\n"


csv.register_dialect('my_dialect', dialect=MyDialect)

with open('data/dialect_HW.csv', 'w') as file:
    writer = csv.writer(file, dialect="my_dialect")
    writer.writerow([i for i in range(7)])
    writer.writerow([i for i in range(7)][::-1])

sniffer = csv.Sniffer()
dialect = None

with open('data/dialect_HW.csv', "r") as file:
    data = file.read()
    dialect = sniffer.sniff(data)
    print(f'delimiter----> {dialect.delimiter} \nquotechar----> {dialect.quotechar}')
