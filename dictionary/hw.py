data = ['John_25', 'Sally_19', 'Susan_35', 'Jack_16']
name_age_dict = {v.split('_')[0]: v.split('_')[1] for v in data}
print(name_age_dict)


matrix = [[j for j in range(2)] for i in range(3)]
print(matrix)

flatten_matrix = [val for sublist in matrix for val in sublist]
print(flatten_matrix)
for i in matrix:
    print(i)
