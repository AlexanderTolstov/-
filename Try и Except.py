def add_everything_up(a, b):
    return a + b
try:
    add_everything_up(123.456, 'строка')
    add_everything_up('яблоко', 4215)
    add_everything_up(123.456, 7)
except TypeError:
    print(add_everything_up(str(123.456), 'строка'))
    print(add_everything_up('яблоко', str(4215)))
    print(add_everything_up(123.456, 7))
