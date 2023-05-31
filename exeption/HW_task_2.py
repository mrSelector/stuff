# Задание 2
# Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание,
# умножение, деление и возведение в степень. Программа должна выдавать сообщения об ошибке и
# продолжать работу при вводе некорректных данных, делении на ноль и возведении нуля в
# отрицательную степень.


class Parser:
    @staticmethod
    def converter_type(value_str):
        result = 0
        try:
            if isinstance(value_str, str):
                if '.' in value_str:
                    result = float(value_str)
                else:
                    result = int(value_str)
        except TypeError:
            print('Error!Enter valid task.e.q "2 + 2": ')
        return result

    def pars(self, task):
        res = tuple(task.split(' '))
        if len(res) < 3:
            print('Error!Enter valid task.e.q "2 + 2": ')
            return 0, 0, '+'
        a, op, b = res
        return self.converter_type(a), self.converter_type(b), op


class Core:
    def __init__(self):
        self.parser = Parser()

    def calculate(self, task):
        a, b, op = self.parser.pars(task)
        try:
            if op == '+':
                return a + b
            elif op == '-':
                return a - b
            elif op == '*':
                return a * b
            elif op == '/':
                return a / b
            elif op == '**':
                return a ** b

        except ZeroDivisionError:
            print('ERROR! Enter your task.e.q "2 + 2": ')
        return 'Error!Enter valid task.e.q "2 + 2": '


class Interface:
    def __init__(self):
        self.core = Core()

    def run(self):
        while True:
            task = input('Enter your task: "e.q 2 + 2": ')
            result = self.core.calculate(task)
            print(result)


interface = Interface()
interface.run()
