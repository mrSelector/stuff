"""Напишите функцию-генератор для получения n первых простых чисел"""


def prime(n):
    for i in range(2, n + 1):
        count = 0
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count == 2:
            values = i
            yield values


for value in prime(77):
    print(value)

it = iter(prime(77))
print(next(it))
print(next(it))
