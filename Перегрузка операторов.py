class Building:
    def __init__(self, numberOfFloors, type):
        self.numberOfFloors = numberOfFloors
        self.type = type
    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.type == other.type

building_1 = Building(numberOfFloors = 99, type = 'Кирпичный')
building_2 = Building(numberOfFloors = 35, type = 'Деревянный')

if building_1 == building_2:
    print('Одинаковые дома')
else:
    print('Разные дома')


