class Base:
    def method(self):
        print('Current class is ',__class__.__name__)
        print('Instans class is ', type(self).__name__)


class Child(Base):
    pass

base = Base()
base.method()


child = Child()
child.method()
Child.method(object)