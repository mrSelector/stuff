import time
x = list(range(10000))
y = list(range(5000, 15000))
q = list(range(10000, 20000))


def some(*args):
    lst = []
    for i in args:
        for j in i:
            if j not in lst:
                lst.append(j)
    return lst


# print(some(x, y, q))

start = time.time()

s = set(x)
t = s.union(set(y), set(q))
r = list(s)
print(r)
stop = time.time() - start
print(stop)
