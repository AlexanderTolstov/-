def apply_all_func(int_list: list, *functions):
    res_dict: dict = {}
    for func in functions:
        res = func(int_list)
        res_dict[func.__name__] = res
    return res_dict


print(apply_all_func([33, 20, 15, 9, 2, 47], max, min, len, sum, sorted))
print(apply_all_func([3, 12, 66, 10, 94], max, min, len, sum, sorted))