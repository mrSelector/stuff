print('calculator')
loop = True
while loop:
    try:
        a = float(input('enter some a: '))
        b = float(input('enter some b: '))
        print(a ** b)
        print('norm')
        loop = False
    except (ZeroDivisionError, ValueError) as e:
        print(e)

    print('zbs')
