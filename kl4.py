class Dom:
    """
    klasa opisujaca Dom
    """

    def __init__(self, metraz, kolor, liczba_okien):
        # usupełnic konstruktor i metody odczytywania pol
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_kolor(self):
        print(f"Mamy kolor {self.__kolor}")

    def podaj_metraz(self):
        print(f"Mamy metraż {self.__metraz}")
        print(type(self.__metraz))

    def podaj_okna(self):
        print(f"Mamy okien {self.__liczba_okien}")

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraż"))
        self.__metraz = wybor

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor


dom1 = Dom("500", "biały", 8)
dom1.podaj_kolor()
dom1.podaj_okna()
dom1.podaj_metraz()

dom1.zmien_metraz()
dom1.podaj_metraz()

dom2 = Dom(700, "zielony", 12)
dom2.zmien_metraz()
dom2.zmien_okna()
dom2.zmien_kolor()
dom2.podaj_metraz()
# 11:20