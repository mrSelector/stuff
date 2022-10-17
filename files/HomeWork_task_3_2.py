import shelve
import os.path


class DataBase:
    def __init__(self):
        self.data = os.path.join('data', 'db.txt')

    def add_link(self, name, url):
        if not name:
            raise KeyError('Name cannot be empty')
        if not url:
            raise ValueError('URL cannot be empty')
        with shelve.open(self.data) as db:
            if name in db:
                raise KeyError('Link does already exist')
            db[name] = url

    def get_link(self, name):
        with shelve.open(self.data) as db:
            return db.get(name, 'The name is not in the database')
