class Cars():
    price = 1000000
    def horse_powers(self):
        self.horse_powers = 150
        print('Лошадинных сил:', self.horse_powers)
    def inspect(self):
        print('Цена машины:', self.price)


class Nissan(Cars):
    price = 2500000
    def horse_powers(self):
        self.horse_powers = 250
        print('Лошадинных сил:', self.horse_powers)
class Kia(Cars):
    price = 500000
    def horse_powers(self):
        self.horse_powers = 100
        print('Лошадинных сил:', self.horse_powers)


print ('Моя машина')
my_car = Cars()
my_car.horse_powers()
my_car.inspect()

print ('Nissan')
my_car = Nissan()
my_car.horse_powers()
my_car.inspect()

print ('Kia')
my_car = Kia()
my_car.horse_powers()
my_car.inspect()