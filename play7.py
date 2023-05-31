class A:
    def __init__(self, password):
        self._password = password
        self.__x = 10

    @property
    def x(self):
        if self._password == "123":
            return self.__x
        return 'zalupa'


a = A("123")
print(a.x)
print(a._password)