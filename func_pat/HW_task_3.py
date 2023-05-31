"""Задание 3
   Создайте функцию-генератор чисел Фибоначчи. Примените к ней декоратор, который будет оставлять в
   последовательности только чётные числа."""


def my_decorator(generator):
    def wrapper(*args):
        sequence = generator(*args)
        return filter(lambda x: x % 2 == 0, sequence)
    return wrapper


@my_decorator
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        yield b


print(list(fibonacci(30)))
