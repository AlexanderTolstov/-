class House:
    def __init__(self):
        self.floors = 0
    def setNewNumbersOfFloors(self, floors):
        self.floors = floors
myhouse = House()
myhouse.setNewNumbersOfFloors(99)
print(myhouse.floors)

