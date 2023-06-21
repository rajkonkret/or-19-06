# dziedziczenie
class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):
    """
    Samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()
        print(f"MArka: {self.marka}")


poj = Pojazd("Czerwony")
poj.info()
poj2 = Samochod("Bialy", "Volvo")
poj2.info()
print(type(poj))
print(type(poj2))
# <class '__main__.Pojazd'>
# <class '__main__.Samochod'>