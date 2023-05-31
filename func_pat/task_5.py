# Створіть список цілих чисел. Отримайте список квадратів непарних чисел із цього списку.

numbers = [i**2 for i in range(10) if i % 2 != 0]

print(numbers)

"""Якщо малось на увазі зробити через lambda вираз"""

lst = [2, 3, 4, 5, 6, 7]

numbers2 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 != 0, lst)))

print(numbers2)
