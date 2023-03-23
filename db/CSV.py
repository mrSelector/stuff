import csv

with open('example1.csv', 'r') as f:
    reader = csv.DictReader(f)
    for i in reader:
        if i['name'] == 'iPhone 5S':
            print('zbs')
        else:
            print(i['name'])


with open('data/out.csv', 'w') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    writer.writerow([1, 2, 3])
    writer.writerow([1, 2, 'Armada'])
    writer.writerow([1, 2, 3])


with open('data/people.csv', 'w') as fi:
    fieldnames = ['Name', 'lastname', 'age']
    writer = csv.DictWriter(fi, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({
        'Name': 'Pashko',
        'lastname': 'Ostrovs`kyi',
        'age': 35})
    writer.writerow({
        'Name': 'Olga',
        'lastname': 'Ostrovs`ka',
        'age': 33})


class CustomDialect(csv.Dialect):
    quoting = csv.QUOTE_ALL
    quotechar = "*"
    delimiter = "!"
    lineterminator = "\n"


csv.register_dialect('test', CustomDialect)

with open('data/testdialect.csv', "w") as d:
    # writer = csv.writer(d, dialect=CustomDialect)
    writer = csv.writer(d, dialect='test')
    writer.writerow([1, 2, 3])
    writer.writerow([1, 2, 3])
    writer.writerow([1, 2, 3])
    writer.writerow([1, 2, 3])

sniffer = csv.Sniffer()
dialect = None

with open('data/testdialect.csv', "r") as f:
    content = f.read()
    dialect = sniffer.sniff(content)
    print(dialect.delimiter, dialect.quotechar, dialect.quoting)

with open('data/testdialect.csv', "r") as f:
    reader = csv.reader(f, dialect=dialect)
    for row in reader:
        print(row)

