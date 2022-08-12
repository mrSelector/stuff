class Car:
    color = 'RED'

    def ride(self):
        print('Lets ride')


my_car = Car()
my_car.color = 'white'
print(my_car.color)
print(my_car.ride())
my_car2 = Car()
my_car2.door_count = 7
print(my_car2.door_count)