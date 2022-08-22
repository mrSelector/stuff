def my_for(iterable):
    it = iter(iterable)
    while True:
        try:
            value = next(it)
            print(value)
        except StopIteration:
            break


my_for(range(33))
my_for('Hello, motherfucker')

