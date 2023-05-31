"""Задание 2
Модифицируйте решение предыдущего задания так, чтобы оно работало не с текстовыми, а бинарными
файлами."""
import random
import os.path
from array import array
numbers = [random.randint(0, 10000) for _ in range(10000)]
b_numbers = array('i', numbers)

with open('binary_file.bin', 'wb') as bin_file:
    bin_file.write(b_numbers)


filesize = os.path.getsize('binary_file.bin')
int_len = array('i').itemsize
read_array = array('i', (0 for _ in range(filesize // int_len)))

with open('binary_file.bin', 'rb') as file:
    w = file.readinto(read_array)

print(read_array)

