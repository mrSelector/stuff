# # city = ['Dnipro', 'Kyiv', 'Odesa']
# # population = [1234, 567, 890]
# # n = list(enumerate(city,1))
# # print(n)
# # for num_city, city in enumerate(city, 1):
# #     print('City', city, 'is', num_city)
# # n = [1, 2, 3, 4, 6]
# # print(*city)
# # print(*n)
# #
# #
# # r = range(20, 2, - 3)
# # print(r[1:3])
# n = 50.5 % 11.56
#
# print(n)

class WordSequence(list):

    _delimiters = ('.', ',', ';', ':', ' -', '- ')

    def __init__(self, text):
        words = [word.casefold() for word in WordSequence._split(text)]
        for word in words:
            if word not in self:
                self.append(word)

    @staticmethod
    def _split(text):
        string = text
        for delimiter in WordSequence._delimiters:
            string = string.replace(delimiter, ' ')
        return string.split()


def main():
    text = '''Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    Quam quidem, veniam dolor ipsum sapiente ullam mollitia molestias 
    repellendus nesciunt voluptas.'''

    words = WordSequence(text)
    for word in words:
        print(word)



if __name__ == '__main__':
    main()