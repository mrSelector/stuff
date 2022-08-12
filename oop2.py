# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def print_info(self):
#         print(self.name, 'is', self.age)
#
#
# pasha = Person('Pashko', 34)
# petro = Person('Petr', 33)
#
# pasha.print_info()
# petro.print_info()
#


class MyObject:
    class_attribute = 3223

    def __init__(self):
        self.data = 7

    def print_data(self):
        print(self.data)

    @staticmethod
    def statprint():
        print(MyObject.class_attribute)

    def normprint(self):
        print(self.data)


MyObject.statprint()

obj = MyObject()
obj.normprint()
obj.statprint()

dd = obj.__dict__.get('data')
dde = obj.__dict__.get('class_attribute')
print(dde)