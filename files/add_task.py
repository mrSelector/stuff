""" Задание
    Создайте список товаров в интернет-магазине. Сериализуйте его при помощи pickle и сохраните в JSON."""
import json
import pickle
import os.path
file_name_pickle = os.path.join('data', 'shop_data')
file_name_json = os.path.join('data', 'shop_data_json')
product_list = ['candy', 'notebook', 'stereo', 'mouse', 'headphones']

with open(file_name_pickle, 'wb') as file:
    pickle.dump(product_list, file)

with open(file_name_pickle, 'rb') as file_:
    data = pickle.load(file_)
    print(data)


with open(file_name_json, 'w') as f:
    json.dump(data, f)

