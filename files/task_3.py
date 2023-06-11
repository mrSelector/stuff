"""Попрацюйте зі створенням власних діалектів,
 довільно вибираючи правила для CSV-файлів.
 Зареєструйте створені діалекти та попрацюйте,
використовуючи їх зі створенням/читанням файлом."""


import csv


class MyDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "|"
    delimiter = "*"
    lineterminator = "\n"


csv.register_dialect('my_dialect', dialect=MyDialect)

with open('dialect_hw.csv', 'w') as file:
    writer = csv.writer(file, dialect='my_dialect')
    writer.writerow([i for i in range(7)])
    writer.writerow([i for i in range(7)[::-1]])

sniffer = csv.Sniffer()

with open('dialect_hw.csv', 'r') as file:
    data = file.read()
    dialect = sniffer.sniff(data)
    print(f'delimiter----> {dialect.delimiter} \nquotechar----> {dialect.quotechar}')

