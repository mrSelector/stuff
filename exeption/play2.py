def main():
    try:
        raise ValueError('Value error')

    except ValueError as error:
        print(error)
        raise


try:
    main()
except ValueError:
    print('error')

class A:
    def __del__(self):
        print('pizda')


a =A()

del a
import warnings
import logging

logging.error('ddd')

warnings.warn('bla bla bla ')
l = [1,2]
a = float(l)
print(a)