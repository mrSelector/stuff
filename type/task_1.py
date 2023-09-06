"""
Створіть функцію, яка приймає список з елементів типу int, а повертає новий список з рядкових значень вихідного масиву.
Додайте анотацію типів для вхідних і вислідних значень функції. """
from typing import List


def list_to_str(int_list: List[int]) -> List[str]:
    return [str(item) for item in int_list]


int_lst = [1, 2, 3, 5, 77, 32, 38]
str_lst = list_to_str(int_lst)
print(str_lst)