tekst = "Witaj świecie"
print(tekst)  # Witaj świecie
tekst2 = tekst.upper()
print(tekst)
print(tekst2)  # WITAJ ŚWIECIE
# str jest niemutowalny
print(tekst.upper())  # WITAJ ŚWIECIE
print(tekst)  # Witaj świecie

tekst3 = tekst.lower()  # zamiana na małe litery
print(tekst3)  # witaj świecie
print(tekst)

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - teksty binarny
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

print(tekst.count("i"))  # 3
print(tekst.count("i", 0, 4))  # od pozycjo 0 do 3 włacznie

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona\b"
print(tekst_format)

# \t tabulator
# \n - nowa linia
# \b - backspace

starszy = "Witaj %s!"
print(starszy % imie)  # Witaj Radek!

print("Witaj {}!".format(imie))  # Witaj Radek!

print("""
    Tekst
        wielolinijkowy
""")
# Tekst
# wielolinijkowy

# ctrl ? (/) - komentowanie zaznaczonego tekstu
