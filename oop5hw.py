class BMW:
    def start_engine(self):
        print("BMW engine has a crude engine sound.")

    def max_speed(self):
        print("BMW max speed is 250 km/h.")


class Ferrari:
    def start_engine(self):
        print("Ferrari engine has a smooth engine sound.")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h.")


def car_details(car):
    car.start_engine()
    car.max_speed()



bmw = BMW()
ferrari = Ferrari()


car_details(bmw)
car_details(ferrari)