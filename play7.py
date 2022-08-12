

from dataclasses import asdict, dataclass
from typing import Any, Dict, List

dataset = [
    ['Ukraine', 'Yura', 33, 'm', 183, 85],
    ['Ukraine', 'Ira', 30, 'f', 163, 55],
    ['Ukraine', 'Yura2', 3, 'm', 183, 85],
]


@dataclass
class Data:
    country: str
    name: str
    age: int
    gender: str
    height: int
    weight: int


class Database:
    """Класс имитирующий работу базы данных"""

    data = []

    def read_data(self, criteria: dict) -> List[Dict[str, Any]]:
        """Считывает данные из списка по поисковому критерию"""
        find_data = []

        for key, val in criteria.items():
            for user in self.data:
                if user[key] == val:
                    find_data.append(user)
            break
        return find_data

    def write_data(self, user: Data) -> None:
        """Записывает данные в псевдо базу"""
        # TODO в идеале реализовать проверку
        # на уникальность данных но для
        # псевдобазы мне показалось это излишним
        self.data.append(
            asdict(
                user,
            ),
        )


db = Database()
for user in dataset:
    db.write_data(Data(*user))


print(db.read_data({'age': 33}))

