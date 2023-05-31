# Створіть звичайну функцію множення двох чисел. Створіть карированну функцію множення двох чисел.
# Частково застосуйте її до одного аргументу, до двох аргументiв.


def multi(x, y):
    return x * y


def curr_multi(x):
    def inner_curr(y):
        return x * y

    return inner_curr


print(multi(7, 8))

multiply = curr_multi(7)
print(multiply(8))

print(curr_multi(7)(8))
