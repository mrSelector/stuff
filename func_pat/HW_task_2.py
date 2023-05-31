""" Задание 2
    Создайте список целых чисел. Получите список квадратов нечётных чисел из этого списка."""

import random

list_numbers = [random.randint(1, 77) for _ in range(38)]
filtered_list = filter(lambda x: x % 2 != 0, list_numbers)
square = list(map(lambda x: x ** 2, filtered_list))
print(square)