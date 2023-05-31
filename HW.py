# 1.Организуйте архитектуру приложения “База данных” (псевдо). В роли базы данных у вас
# будет класс Database, который будет хранить данные в виде переменной списка.
# 2. Класс Database должен иметь методы read_data(criteria), write_data(element).
# 3. Для элемента данных напишите класс Data. В данном случае мы будем хранить данные о
# пользователях. Data будет иметь атрибуты: country, name, age, gender, height, weight.
# 4. В классе Database метод read_data будет принимать на вход аргумент criteria, который
# является словарем вида {“age”: 25}, после чего метод вернет отдельный список всех
# элементов у которых данное условие истино.
# Подсказка: чтобы получить у объекта класса значение его атрибута как у словаря, используйте
# следующий синтаксис: your_class_instance.__dict__.get(‘name’).
# PS: организуйте правильную инкапсуляцию. Вы должны добавлять элементы в класс Database
# только через метод write, но никак не напрямую через атрибут elements.


class Database(object):


    def read_data(self, criteria):
        data = []
        pass

    def write_data(self, element):
        pass


class Data(object):
    def __init__(self, country, name, age, gender, height, weight):
        self.country = country
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def __str__(self):
        return 'Country: {}, Name: {}, Age: {}, Gender: {}, Height: {}, Weight: {}'.format(self.country, self.name,
                                                                                           self.age, self.gender,
                                                                                           self.height, self.weight)


pashko = Data('Ukraine', 'Pashko', 34, 'Male', 18.5, 186)
olya = Data('Ukraine', 'Olga', 32, 'Female', 18.5, 186)
db = [pashko, olya]
print(db)

