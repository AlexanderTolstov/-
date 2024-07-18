def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result <= 1:
            print("Составное")
        if result == 2:
            print("Простое")
        for i in range(2, int(result ** 0.5) + 1):
            if result % i == 0:
                print("Составное")
            else:
                print("Простое")
            return result
    return wrapper
@is_prime
def sum_three(*args):
    return sum(args)
result = sum_three(2, 3, 9)
print(result)
result = sum_three(12, 3, 5)
print(result)
result = sum_three(3, 3, 5)
print(result)
result = sum_three(8, 3, 5)
print(result)
result = sum_three(9, 3, 5)
print(result)