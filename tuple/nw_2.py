"""Задание
Напишите программу, которая вводит с клавиатуры последовательность чисел и выводит её
отсортированной в порядке возрастания."""


numbers = input('Enter numbers: ')


def sorted_(*args):
    lst = []
    for item in args:
        lst.append(item)
    lst.sort()
    return lst


print(sorted_(numbers))
