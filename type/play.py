from typing import List


class User:
    def __init__(self, first_name: str, last_name: str):
        self.firs_name = first_name
        self.last_name = last_name

    # def get_full_name(self):
    #     return self.firs_name + " " + self.last_name


def create_user_v1(first_names: list, last_names: list) -> list:
    users = []
    for first_name, last_name in zip(first_names, last_names):
        users.append(User(first_name, last_name))
    return users


def create_user_v2(first_names: List[str], last_names: List[str]) -> List[User]:
    users = []
    items = zip(first_names, last_names)
    for first_name, last_name in items:
        users.append(User(first_name, last_name))
    return users


user1 = create_user_v1(['Petro', 'test'], [777, 333])
user2 = create_user_v2(['Petro', 'test1'], [777, 333])
# print(user2[0].get_full_name())
