"""Задание 3
Напишите программу, которая вводит с клавиатуры текст и выводит отсортированные по алфавиту слова
данного текста."""
texts = str(input('Enter text: '))

delimiters = ('.', ',', ';', ':', ' -', '- ', '<', '>', '!', '?')


def symbol_clear(text, symbols):
    string = text
    for symbol in symbols:
        string = string.replace(symbol, ' ')

    return string.split()


def str_lower():
    lst = []
    for i in clear_text:
        lst.append(i.casefold())
    return lst


clear_text = symbol_clear(texts, delimiters)
lover_text = str_lower()
lover_text.sort()
print(lover_text)
