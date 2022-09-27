user = {
    "name": "JohnDoe",
    "info": {
        "basic": {
            "age": 25,
            "salary": 5000
        },
        "additional": {
            "study": "mathematics",
            "family": "married"
        },
        "special": {
            "projects": [
                {"name": "quantum_computer", "stage": "in_progress"},
                {"name": "laser_gun", "stage": "in_production"}
            ]
        }
    }
}


def get_data(data_dict, keys):
    data = data_dict
    for key in keys:
        data = data[key]
    print(data)


def get_data_rec(data_dict, keys, index=0):
    if index < len(keys):
        return get_data_rec(data_dict[keys[index]], keys, index + 1)
    return data_dict


print(get_data_rec(user, ['info', 'special', 'projects', 0, 'name']))
matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)