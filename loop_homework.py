# def password_checker(corr_pass, attempts=4):
#     for i in range(attempts):
#         password = input('Enter password: ')
#         if corr_pass == password:
#             return 'Success'
#
#     else:
#         return 'Access Denied'
#
#
# result = password_checker('zalupa', attempts=2)
# print(result)

a = 7
b = 14

for i in range(a + 1, b + 1):
    a = a + i
    print(a)

x = int(input('Enter number: '))
y = 1
for i in range(y, x + 1):
    y = y * i
    print(y)

for i in range(7):
    for _ in range(i):
        print('*', end='')
    print(" ")