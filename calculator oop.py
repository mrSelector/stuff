class Parser:

    @staticmethod
    def converter_type(value_str):
        result = 0
        if isinstance(value_str, str):
            if '.' in value_str:
                result = float(value_str)
            else:
                result = int(value_str)
        return result

    def pars(self, expression):
        values = tuple(expression.split(' '))
        a, op, b = values
        return self.converter_type(a), self.converter_type(b), op


class Core:
    def __init__(self):
        self.parse = Parser()
        self.functions = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: a / b,
            "*": lambda a, b: a * b
        }

    def calculate(self, expression):
        a, b, op = self.parse.pars(expression)
        result = self.functions.get(op)(a, b)
        return result


class Interface:
    def __init__(self):
        self.core = Core()

    def run_calculator(self):
        while True:
            print("Enter your expression: eg. '2 + 2' ")
            expression = input()
            result = self.core.calculate(expression)
            print("result: {}".format(result))


inter = Interface()
inter.run_calculator()