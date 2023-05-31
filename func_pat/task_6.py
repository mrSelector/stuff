# Створіть функцію-генератор чисел Фібоначчі. Застосуйте до неї декоратор,
# який залишатиме в послідовності лише парні числа.

def numbers_decorator(generator):
    def wrapper():
        for number in generator():
            if number % 2 == 0:
                yield number
    return wrapper


@numbers_decorator
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fibonacci = fibonacci_generator()
for _ in range(10):
    print(next(fibonacci))
