# klasy
class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def podaj_wiek(self):
        print("Mam", self.wiek, "lat")


print(print.__doc__)
print(Human.__doc__)  # wyswietlenie dokumentacji dla klasy Human

cz1 = Human()
print(cz1.plec)
cz1.imie = "Ania"
print(cz1.imie)
cz1.powitanie()  # Nazywam się Ania
print(type(cz1))  # <class '__main__.Human'>
print(cz1)  # <__main__.Human object at 0x000001D6799F1D50>
cz1.wiek = 56
print(cz1.wiek)
cz1.podaj_wiek()  # Mam 56 lat

cz2 = Human()
cz2.imie = "Radek"
cz2.plec = "m"
cz2.wiek = 34
print(cz2.plec)
cz2.powitanie()
cz2.podaj_wiek()
