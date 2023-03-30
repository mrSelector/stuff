"""1.Напишите рекурсивную функцию, чтобы сгенерировать и вернуть список от 1 до N.
Аргументом функции является только N."""
lst = []


def rec_list(n):
    if n:
        lst.append(n)
        rec_list(n - 1)
    return sorted(lst)


print(rec_list(5))
"""2.Напишите функцию, которая рекурсивно ищет в сложном объекте значение. Сложный
объект — это будет список списков списков и т.д. Например, [1, 2, [3, 4, [5, [6, []]]]]. Функция
должна рекурсивно заходить внутрь вложенных массивов, а если это другой тип данных
игнорировать его."""

obj = [1, 2, [3, 4, [5, [6, []]]]]


def rec_search(lst, value):
    for item in lst:
        if isinstance(item, list) and len(item) > 0:
            result = rec_search(item, value)
            if isinstance(result, str):
                if result == 'value in list':
                    return result

        if isinstance(item, int):
            if item == value:
                return 'Value in list '
    return False


print(rec_search(obj, 1))