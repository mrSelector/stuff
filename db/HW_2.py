"""Задание 2
Создайте XML файл с вложенными элементами и воспользуйтесь языком поиска XPATH.
Попробуйте осуществить поиск содержимого по созданному документу XML, усложняя свои
запросы и добавляя новые элементы, если потребуется."""
from xml.etree import ElementTree

tree = ElementTree.parse('data/some.xml')
root = tree.getroot()

# for i in root:
#     print(i.attrib.get('car'))
#     for j in i:
#         print(f"{j.tag}----> {j.text}")

for child in root:
    print(child.find('model').text)
