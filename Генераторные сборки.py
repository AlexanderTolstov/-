#Задача 1: Фабрика Функций
def create_operation(operation):
    if operation == "multiply":
        def add(x, y):
            return x * y
        return add
    elif operation == "division":
        def subtract(x, y):
            return x // y
        return subtract
my_func_multiply = create_operation("multiply")
my_func_division = create_operation("division")
print(my_func_multiply(8,2))
print(my_func_division(8, 2))

#Задача 2: Лямбда-Функции
multiply = lambda x, y: x ** y
print(multiply(21, 3))
def multiply(x, y):
   return x ** y
print(multiply(21, 3))

#Задача 3: Вызываемые Объекты
class Rect():
    def __init(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, a, b):
        return a * b
rect = Rect()
print(rect(6, 4))

