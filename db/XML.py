from xml.etree import ElementTree as ET
#
# tree = ET.parse('data/test.xml')
# root = tree.getroot()
# for child in root:
#     print(F"PK ---> {child.attrib.get('pk')}")
#     for user in child:
#         print(user.tag.replace('_', ' ').title(), user.text)
#
#
# root = ET.Element('Record')
# for i in range(10):
#     sub_element = ET.SubElement(root, f'value_{i}')
#     sub_element.text = str(i * 10)
#
# tree = ET.ElementTree(root)
# tree.write('data/outtest.xml', encoding='utf8')
#
# data = [
#     {'x': 10, 'y': 20, 'c': 30},
#     {'x': 11, 'y': 21, 'c': 31},
#     {'x': 12, 'y': 22, 'c': 32},
#     {'x': 13, 'y': 23, 'c': 33}
#     ]
#
# root = ET.Element('coordinate')
# for row in data:
#     sub_element = ET.SubElement(root, 'record')
#     for key, value in row.items():
#         e = ET.SubElement(sub_element, key)
#         e.text = str(value)
#
# tree = ET.ElementTree(root)
# tree.write('data/coordinate.xml', encoding='utf8')
#
