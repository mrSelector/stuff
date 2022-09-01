"""Задание 1
Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог
reversed)."""


class MyIterReverse:
    def __init__(self, iterable):
        self.iter = iterable
        self.index = len(iterable)-1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        res = self.iter[self.index]
        self.index = self.index - 1
        return res


lst = [1, 3, 4, 7, 8, 33, 6]

for i in MyIterReverse(lst):
    print(i)
