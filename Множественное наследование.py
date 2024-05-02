class Vehicle():
    vehicle_type = "none"
class Cars():
    price = 1000000
    def horse_powers(self):
        return 210
class Nissan(Vehicle, Cars):

    pass
car = Nissan
print (car.horse_powers(self=Cars))
print (car.vehicle_type, car.price)
