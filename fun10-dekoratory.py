def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()  # tu jawnie wykonuje funkcje, ktora przyjdzie

    return wew  # zwracy adres funkcji, nie wykonujemy funkcji


@dekor
def hej():
    print("Hej")

@dekor
def dodawanie():
    print(1 + 2)


hej()
dodawanie()
