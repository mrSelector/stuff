"""Задание 2
Перепишите решение первого задания с помощью генератора."""


def revers(iterable):
    index = len(iterable) - 1
    yield iterable[index]
    index -= 1


lst = [1, 3, 4, 7, 8, 33, 6]

for i in revers(lst):
    print(i)
