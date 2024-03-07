immutable_var = 1, 2, 3, 'a', 'b', 'c'
print(immutable_var)
immutable_var[1] = 23
# Значение элементов кортежа нельзя изменить т.к. кортеж не поддерживает обращение по элементам. И при выполнении
# программы выйдет ошибка.

mutable_list = ['Arsenal', 'Chelsea', 'Liverpool', 'Everton']
print (mutable_list)
mutable_list[1] = 'Barcelona'
print(mutable_list)

