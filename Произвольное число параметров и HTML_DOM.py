def test_1(*args):
    for i in enumerate(args):
        print('Место:', i)

test_1(45, 'Приветствие', False, 69, 'Салам', 79034121233456462456768)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n=n - 1)

print (factorial(7))
print (factorial(1))
print (factorial(5))
print (factorial(0))
print (factorial(125))
print (factorial(6))
print (factorial(99))
print (factorial(100))
print (factorial(87))
print (factorial(256))
