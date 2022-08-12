my_list = [1, 2, 3, 4, 5, 33, 45, 64, 24, 5]
my_list2 = [22, 4, 6, 31, 5, 7, 64]
my_list3 = []
for value in my_list:
    if value > 5:
        print(value)
print()

for i in my_list2:
    if i in my_list:
        my_list3.append(i)
print(my_list3)

my_list.reverse()
print(my_list)
    
my_list4 = list(range(7))
print(my_list4)