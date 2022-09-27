people = {
    'Pashko': 32233,
    'Ara': 44444,
    'ment': 77777
}
users = {
    'you': 'www.http//youtube.com',
    'pisya': 18.5
}

print(users['pisya'])
# print(people.items())
# print(people.keys())
# print(people.values())
# people.update(users)
# print(people.get('pisy','zalupu'))
# print(people)
#
res = 0

while True:
    val = input('what wont?: ')
    if val == 'end':
        break
    res = res + people[val]
    print(res)


