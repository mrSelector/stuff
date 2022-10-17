from array import array
import os.path
file_size = os.path.getsize('binary_file.bin')
len_ = array('i').itemsize
list_read = array('i', (0 for _ in range(file_size // len_)))
with open('binary_file.bin', 'rb') as file:
    file.readinto(list_read)
# print(list_read)
sum_ = 0
for num in list_read:
    sum_ += num

print(f'Sum numbers is {sum_}')
