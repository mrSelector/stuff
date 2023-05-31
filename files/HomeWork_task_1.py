"""Задание 1
Напишите скрипт, который создаёт текстовый файл и записывает в него 10000 случайных
действительных чисел. Создайте ещё один скрипт, который читает числа из файла и выводит на экран их
сумму."""
import random
random_numbers = [random.randint(0, 10000) for _ in range(10000)]
with open('numbers.txt', 'w') as file_txt:
    for num in random_numbers:
        print(num, file=file_txt)
