class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Menedzer(Pracownik):
    """
    dokumentacja
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.premia + self.pensja


pracownik = Pracownik("Jan", "Kowalski", 7000)
pracownik.przedstaw_sie()
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: wynagrodzenie {wyn_prac}")

menago = Menedzer("Anna", "Nowak", 8000, 2000)
menago.przedstaw_sie()  # Cześć, jestem Anna Nowak
wyn_menago = menago.oblicz_pensje()
print(f"Wynagrodzenie dla menadżera {menago.imie} {menago.nazwisko}: wynagrodzenie {wyn_menago}")
