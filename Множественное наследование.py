class Vehicle():
    vehicle_type = "none"
class Cars():
    price = 1000000
    def horse_powers(self):
        return 210
    def inspect(self):
        print('Цена машины:', self.price)

class Nissan(Vehicle, Cars):
    price = 2500000
    vehicle_type = "Легковой автомобиль"
    def horse_powers(self):
        self.horse_powers = 250
        print('Лошадинных сил:', self.horse_powers)
        print("Тип Авто:", self.vehicle_type)

print ('Nissan')
my_car = Nissan()
my_car.horse_powers()
my_car.inspect()
