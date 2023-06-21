class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def drive(self):
        print('Jadę pojazdem')


class Car(Vehicle):
    def drive(self):
        print('Jade samochodem')


class Bike(Vehicle):
    def drive(self):
        print("Jade rowerem")


class HybridCar(Car, Bike):
    def drive(self):
        super().drive()
        Bike.drive(self)
        print("Jadę pojazdem hybrydowym")


ca1 = Car("Polonez")  # Jade samochodem
ca1.drive()

rower = Bike("Romet")
rower.drive()  # Jade rowerem

hyb = HybridCar("Toyota")
hyb.drive()
print(HybridCar.__mro__)
# (<class '__main__.HybridCar'>, <class '__main__.Car'>, <class '__main__.Bike'>, <class '__main__.Vehicle'>, <class 'object'>)
