m = {x ** 2 for x in range(10)}
print(type(m))
print('\n'.join([str(i) for i in m]))
options = {
    'sep': '-----',
    'end': '\n-------\n'
}

print(2, 3, **options)
print()

# gen = [2 ** i for i in range(1, 11)]
# print(gen)
#
#
# class NW(list):
#     def __getitem__(self, item):
#         if item > 0:
#             return super().__getitem__(item - 1)
#         elif item == 0:
#             raise IndexError('List index out of range')
#         elif item < 0:
#             return super().__getitem__(item)
#
#
# nw = NW(gen)
# print(nw[0])
