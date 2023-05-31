# def Person(name, age):
#     def print_name():
#         print(f'Hello!,my name is {name}')
#
#     def get_age():
#         return age
#
#     return {'print_name': print_name, 'age': get_age}
#
#
# pashko = Person('Pashko', 34)
# pashko['print_name']()
# print(pashko["age"]())
#
#
from functools import reduce

lst = [4, 4, 7, 4, 1, -1, 8, 9, 3]

result = list(map(lambda x: x * 2, lst))
for i in result:
    print(i)

positive = list(filter(lambda x: x > 0, lst))
print(positive)

product = reduce(lambda x, y: x * y, positive)
print(product)

print((lambda x:-x)(5))
print(str(True))
