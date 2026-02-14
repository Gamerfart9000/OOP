class Vehicle:
    def __init__(self, name, fare):
        self.name = name
        self.fare = fare


class Bus(Vehicle):
    def get_fare(self):
        return self.fare 


bus = Bus("City Bus", 100)
print("Total Bus Fare:", bus.get_fare())