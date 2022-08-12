import functools
@functools.lru_cache(maxsize= None)
def fibbonachi(n):

    if n == 2 or n == 1:
        return 1
    else:
        return fibbonachi(n - 1) + fibbonachi(n - 2)


for i in range(1, 6):

    print(fibbonachi(i))

count_step = int(input('Введите количество ступенек: '))

@functools.lru_cache(maxsize= None)
def steps(n):
    if n == 1 or n == 2:
        return 1
    else:
        return steps(n - 1) + steps(n - 2)


print(steps(count_step))


