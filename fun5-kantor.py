def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota):
        print(f"Wymieniam dolary ${kwota} = {kwota * 4.1} zł")

    def eur(kwota):
        print(f"Wymieniam euro EUR {kwota} = {kwota * 4.43} zł")

    if waluta == 'eur':
        return eur
    else:
        return usd


kantor_eur = kantor('eur')
print(kantor_eur)  # <function kantor.<locals>.eur at 0x000001F30C13DF80>
kantor_eur(1000)  # Wymieniam euro EUR 1000 = 4430.0 zł

kantor_usd = kantor('usd')
kantor_usd(5000)  # Wymieniam dolary $5000 = 20500.0 zł

