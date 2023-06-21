# wielodziedziczenie
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z kalsy B")


class C(B, A):
    """
    klasa C, dziedziczy po klasie A i B
    """

    def method(self):
        super().method()  # Metoda z kalsy B
        print(f"Metoda z klasy C")
        A.method(self)  # Metoda z klasy A


a = A()
a.method()

b = B()
b.method()

c = C()
c.method()
print(C.__mro__)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
#13:25