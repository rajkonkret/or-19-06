class Human:
    """
    Klasa Human opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, wzrost, plec="k"):
        self.imie = imie
        self.wiek = wiek
        self.wzrost = wzrost
        self.plec = plec

    def powitanie(self):
        print(f"Nazywam się {self.imie}")

    def moj_wiek(self):
        print("Mam", self.wiek, "lat")

    def moj_wzrost(self):
        print("Nazywam się", self.imie, "Mam", self.wzrost, "cm wzrostu")

    def ruszaj(self):
        if self.plec == "m":
            print("Ruszyłem")
        else:
            print("Ruszyłam")


cz1 = Human("Radek", 80, 180, "m")
print(cz1.imie)
print(cz1.plec)
cz1.ruszaj()

cz2 = Human("Ania", 34, 170)
print(cz2.plec)  # k
cz2.ruszaj()
cz2.moj_wiek()
cz2.moj_wzrost()
