# hermetyzacja, enkapsulacja

class Car:
    """
    Klasa samochod
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # oznaczenie pola jako prywatne
        self.__predkosc = 0

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Prędkość wynosi", self.__predkosc, "km/h")

    def hamuj(self):
        """
        funkcja hamuj, zmniejsza predkosc o 10 za każym wywołaniem
        :return: None
        """
        self.__predkosc -= 10

    def __zmien_bieg(self):
        print("Zmiana biegu")


ca1 = Car("Mercedes", 2023)
print(ca1.model)
ca1.gaz()
ca1.gaz()
ca1.gaz()
ca1.gaz()
ca1.gaz()
# print(ca1.__predkosc)  # 50
ca1.licznik()  # Prędkość wynosi 50 km/h
ca1.__predkosc = 120
ca1.licznik()  # Prędkość wynosi 50 km/h

ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.hamuj()
ca1.licznik()  # Prędkość wynosi 0 km/h
print(ca1.__predkosc)  # 120
