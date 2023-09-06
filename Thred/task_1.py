"""Створіть функцію для обчислення факторіала числа. Запустіть декілька завдань, використовуючи Thread,
 і заміряйте швидкість їхнього виконання, а потім заміряйте швидкість обчислення, використовуючи той же набір завдань
  на ThreadPoolExecutor. Як приклади використовуйте останні значення, від мінімальних і до максимально можливих,
   щоб побачити приріст або втрату продуктивності."""

import threading
import concurrent.futures
import time

numbers = [100000, 150000, 17000, 300000]


def factorial(f_num):
    """Функція обчислювання числа"""

    result = 1
    for i in range(1, f_num + 1):
        result = result * i
    return result


def time_decorator(func):
    """Декоратор для заміру часу виконання"""

    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        print(f'Run time {func.__name__} ---> {time.time() - start_time} sec')

    return wrapper


@time_decorator
def run_thread():
    """Функція створює потоки та приєднює іх за допомогою Thread"""
    for num in numbers:
        tread = threading.Thread(target=factorial, args=(num,))
        tread.start()
        tread.join()


@time_decorator
def run_thread_pool():
    """Функція створює потоки, добаляє їх у пул та виконує за допомогою ThreadPoolExecutor """
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(factorial, numbers)


if __name__ == '__main__':
    run_thread()
    run_thread_pool()
