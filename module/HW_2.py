class DataBase:
    def __init__(self):
        self.db = {}

    def get_db(self, name):
        return self.db.get(name, 'The name is not in the database')

    def set_db(self, name, url):
        if not name:
            raise KeyError('Name cannot be empty')
        if not url:
            raise ValueError('URL cannot be empty')
        if name in self.db:
            raise KeyError('Link already exists')

        self.db[name] = url
