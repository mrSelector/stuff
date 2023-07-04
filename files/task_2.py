"""Створіть XML-файл із вкладеними елементами та скористайтеся мовою пошуку XPATH.
 Спробуйте здійснити пошук вмісту за створеним документом XML, ускладнюючи свої запити
та додаючи нові елементи,  якщо буде потрібно."""

from xml.etree import ElementTree

tree = ElementTree.parse('data/some.xml')
root = tree.getroot()

for i in root:
    print(i.attrib.get('car'))
    for j in i:
        print(f"{j.tag}----> {j.text}")

for child in root:
    print(child.find('model').text)
