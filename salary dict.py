class Core:
    def __init__(self):
        self._types = {
            'A': 100,
            'B': 200,
            'C': 300
        }

    def get_salary(self, type_class):
        return self._types.get(type_class, 0)


class AccountingInterface:
    def __init__(self, data):
        self.core = Core()
        self.database = data

    def get_salary(self, name):
        type_work = self.database.get(name)
        salary = self.core.get_salary(type_work)
        return salary


db = {'Ivan':'A', 'Olya': 'B', "Pashko": 'C'}
interface = AccountingInterface(db)
res = interface.get_salary('Olya')
print('Salary Olya:', res)