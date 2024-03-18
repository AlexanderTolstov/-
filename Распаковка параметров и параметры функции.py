def print_params(a = 1, b = 'string', c = True):
    print(a, b, c)
values_list = [3, 'word', False]
values_dict = {'a': 3, 'b' : 'word', 'c' : False}
values_list_2 = [25, 'happy']

print_params(b = 25)
print_params(c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)