from xml.etree import ElementTree as ET

tree = ET.parse('data/test.xml')
root = tree.getroot()
for child in root:
    print(child.find('first_name').text)
    print(child.find('last_name').text)
    print(child.find('age').text)
    print()

name = root.findall('./person/first_name')
last_name = root.findall('./person/last_name')
age = root.findall('./person/age')

for items in zip(name, last_name, age):
    row = {item.tag: item.text for item in items}
    print(row)

first_name = root.find('./person/age/..[@pk][1]/first_name').text
last_name = root.find('./person/age/..[@pk][2]/last_name').text
age = root.find('./person/age/..[@pk][3]/age').text
print(first_name, last_name, age)
