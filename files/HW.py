"""1.Cкачайте таблицу данных в виде csv файла по ссылке.
2. Прочитайте файл и преобразуйте его в список словарей, где ключами будут имена
колонок, а значения — это данные из списков.
3. Сохраните полученный список словарей в JSON файл.
4. По аналогии с примером 4 на уроке, сделайте свой автоматический генератор XML, где
вместо юзеров будут данные о людях в полученном вами JSON файле. Сохраните
полученный XML."""
import csv
import json
from xml.etree import ElementTree

with open('titanic.csv', 'r') as csv_file:
    rows = csv.DictReader(csv_file)
    data = [row for row in rows]


with open('file_json.json', 'w') as json_file:
    json.dump(data, json_file)








with open('file_json.json', 'r') as file:
    tit = json.load(file)

columns = list(tit[0].keys())

rows = []
for user in tit:
    rows.append(list(user.values()))

xml_data = ElementTree.Element('data')
items = [ElementTree.SubElement(xml_data, 'info') for _ in range(len(tit))]
for j in range(len(tit)):
    item = items[j]
    for k in range(len(columns)):
        item.set(columns[k], rows[j][k])

xml_file = ElementTree.tostring(xml_data)
with open('users.xml', 'wb') as file:
    file.write(xml_file)

