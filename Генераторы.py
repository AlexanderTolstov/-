import itertools
def all_variants(text):
    temp_list = []
    for list_1 in range(1, len(text) + 1):
        temp_list.append(list(itertools.combinations(text, list_1)))
    for list_2 in temp_list:
        for list_3 in list_2:
            if ''.join(list_3) != 'ac':
                yield ''.join(list_3)
a = all_variants("abc")
for i in a:
    print(i)