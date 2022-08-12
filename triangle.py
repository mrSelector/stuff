# n = 77
# l = []
# x = 0
# for i in range(2, n + 1,):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         l.append(i)
# print(l)

# print("""Вывести сумму или произведение постых чисел?
# 1.Сумма
# 2.Произведение
# """)
# while True:
#     q =  input()
#     if q == '1': 
#         for s in l:
#             x += s
#         print('Сумма простых чисел =', x)
#         break
#     if q == '2':
#         for s in l:
#             x += s
#         print('Произведение простых чисел =', x)
#         break
#     else:
#         print("Не корректній ввод")



rows = int(input('rows?'))
k = 2 * rows - 2
for i in range(0, rows):
    for j in range(0,k):
        print(end=' ')
    k = k - 2
    for j in range(0, i + 1):
        print('* ',end='  ')
    print('')