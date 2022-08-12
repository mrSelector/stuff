class Pars:
    @staticmethod
    def __converter_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if '.' in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def parser(self, expression):
        value = tuple(expression.split(' '))
        if len(value) < 3:
            print('Enter valid expression')
            return 0, 0, '+'
        a, op, b = value
        return self.__converter_type(a), self.__converter_type(b), op


class Core:
    def __init__(self):
        self.pars = Pars()
        self.functions = {'+': lambda a, b: a + b,
                          '-': lambda a, b: a - b,
                          '/': lambda a, b: a / b,
                          '*': lambda a, b: a * b
                          }

    def calculate(self, expression):
        a, b, op = self.pars.parser(expression)
        result = self.functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self.core = Core()

    def run_calculate(self):
        while True:
            print('Enter your expression:'"e.q 2 + 2")
            expression = input()
            result = self.core.calculate(expression)
            print('Result: {}'.format(result))
            print('=' * 20)


interface = Interface()
interface.run_calculate()
