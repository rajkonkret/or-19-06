class Animal:

    def __init__(self, name):
        self.name = name

    def wydaj_odglos(self):
        pass  # nic nie rob

    def info(self):
        print(f"Imie: {self.name}")


class Dog(Animal):
    def __init__(self, name, rasa):
        super().__init__(name)
        self.rasa = rasa

    def wydaj_odglos(self):
        print("Hau Hau")

    def info(self):
        super().info()
        print(f"Rasa: {self.rasa}")


class Cat(Animal):
    def __init__(self, name, kolor):
        super().__init__(name)
        self.kolor = kolor

    def wydaj_odglos(self):
        print("Miau Miau")

    def info(self):
        super().info()
        print(f"Kolor: {self.kolor}")


class Tiger(Cat):
    def __init__(self, name, kolor, liczba_paskow):
        super().__init__(name, kolor)
        self.liczba_paskow = liczba_paskow

    def wydaj_odglos(self):
        print("Arr Arr!!!")

    def info(self):
        super().info()
        print(f"Liczba pasków: {self.liczba_paskow}")


zwierzak = Animal("Bezimienny")
zwierzak.info()
zwierzak.wydaj_odglos()

pies = Dog("Burek", "Kundel")
pies.info()
pies.wydaj_odglos()

kotek = Cat("Filemon", "Biały w ciapy")
kotek.info()
kotek.wydaj_odglos()

tygrysek = Tiger("Rajah", "Pomarańczowy", 15)
tygrysek.info()
tygrysek.wydaj_odglos()
