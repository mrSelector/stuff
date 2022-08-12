class Animal(object):
    def __init__(self):
        self.fly = False
        self.run = False

    def print_atribut(self):
        print('Name instance :', type(self).__name__)
        print('Can fly :', self.fly)
        print('Can run :', self.run)
        print()


class Horse(Animal):
    def __init__(self):
        super().__init__()
        self.run = True


class Bird(Animal):
    def __init__(self):
        super().__init__()
        self.fly = True


class Pegas(Horse,Bird):
    pass

animal = Animal()
animal.print_atribut()

horse = Horse()
horse.print_atribut()

bird = Bird()
bird.print_atribut()

pegas = Pegas()
pegas.print_atribut()


print(Pegas.__mro__)
