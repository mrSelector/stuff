# x = int(input('Enter number: '))
# count = 0
# y = 1
# while count < x:
#     count += 1
#     y = y * count
#     print(y)
# else:
#     print(y)


x = ''
while len(x) < 5:
    word = input('Enter letter or word :')
    if word == 'o':
        continue
    x = x + word
    print(x)
else:
    print(x)

