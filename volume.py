import math

PI = math.pi

def radius():
    a = int(input('Enter radius in sm: '))
    r = a / 2
    
    return r

def height():
    b = int(input('Enter height in sm:'))
    
    return b

def volume():

    r = radius()
    h = height()
    s = PI * r**2
    v = s * h
    return v

print(volume())