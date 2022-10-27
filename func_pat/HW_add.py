"""Задание
Создайте обычную функцию умножения двух чисел. Частично примените её к одному аргументу.
Создайте каррированную функцию умножения двух чисел. Частично примените её к одному аргументу."""
from functools import partial


def multiply(x, y):
    return x * y


def car_multiply(x):
    def _multiply(y):
        return x * y
    return _multiply


multiply_to_seven = partial(multiply, 7)
print(multiply_to_seven(4))
multiply_to_nine = car_multiply(8)
print(multiply_to_nine(4))
