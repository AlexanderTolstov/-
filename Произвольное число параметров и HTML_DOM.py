def test_1(*args):
    for i in enumerate(args):
        print('Место:', i)

test_1(45, 'Приветствие', False, 69, 'Салам', 79034121233456462456768)

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n=n - 1)

print (factorial(7))
print (factorial(1))
print (factorial(5))
