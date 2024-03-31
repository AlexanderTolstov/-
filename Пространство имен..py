def test_function():
    def inner_function():
        print ('Я в области видимости функции test_function')
    inner_function()

test_function()

inner_function() # Данная строчка кода работать не будет, так как эта функция находится в локальном пространстве имен,
# и вызвать ее вне данного пространства нельзя.
