# Напишіть декоратор, який буде для переданої функції заміряти час виконання.
# Напишіть програму яка буде виводити 25 перших чисел Фібоначі, використовуючи
# для цього три наведені в тексті заняття функції - без кеша, з кешем довільної
# довжини, з кешем з модулю functools з максимальною кількістю 10 елементів та з кешем
# з модулю functools з максимальною кількістю 16 елементів.
# За допомогою написаного Вами декоратора заміряйте і порівняйте швидкість роботи
# ціх трьох варіантів.

import time
import functools


def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        return f'Run time {func.__name__} ---> {time.time() - start_time} sec'

    return wrapper


@time_decorator
def fibonacci_no_cash(num):
    if num < 2:
        return num
    return fibonacci_no_cash(num - 1) + fibonacci_no_cash(num - 2)


print(fibonacci_no_cash(35))


def my_cache(function):
    __cache = {}

    @functools.wraps(function)
    def _cached_function(*args):
        cache_value = __cache.get(args)

        if cache_value is None:
            cache_value = function(*args)
            __cache[args] = cache_value

        return cache_value

    return _cached_function


@time_decorator
@my_cache
def fibonacci_my_cash(num):
    if num < 2:
        return num
    return fibonacci_my_cash(num - 1) + fibonacci_my_cash(num - 2)


print(fibonacci_my_cash(35))


@time_decorator
@functools.lru_cache(maxsize=10)
def fibonacci_rlu_cash_10(num):
    if num < 2:
        return num
    return fibonacci_rlu_cash_10(num - 1) + fibonacci_rlu_cash_10(num - 2)


print(fibonacci_rlu_cash_10(35))


@time_decorator
@functools.lru_cache(maxsize=16)
def fibonacci_rlu_cash_16(num):
    if num < 2:
        return num
    return fibonacci_rlu_cash_16(num - 1) + fibonacci_rlu_cash_16(num - 2)


print(fibonacci_rlu_cash_16(35))
