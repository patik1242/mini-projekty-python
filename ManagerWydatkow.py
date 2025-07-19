print("Manager wydatkow")

wydatki = {}

def dodaj():
    data = input("Podaj date (rrrr-mm-dd): ")
    nazwa = input("Podaj nazwe wydatku: ").strip().title()
    kwota = float(input("Kwota: "))
    kategoria = input("Kategoria: ").strip().title()
    nowy = {"nazwa": nazwa, "kwota": kwota, "kategoria": kategoria}
    if data in wydatki:
        wydatki[data].append(nowy)
    else:
        wydatki[data] = [nowy]
    print("Wydatek dodany")

def pokaz_wszystkie_wydatki():
    for data, wartosc in wydatki.items():
        for w in wartosc:
            print(f"- {w['nazwa']}, {w['kwota']} PLN ({w['kategoria']})")

def pokaz_kategoria():
    kategoria = input("Podaj kategorie: ").strip().title()
    znaleziono = False
    for data, wartosc in wydatki.items():
        for w in wartosc:
            if kategoria in w['kategoria']:
                print(f"{data} - {w['nazwa']}: {w['kwota']} PLN")
                znaleziono = True
    if not znaleziono:
        print("Nie ma takiej kategorii")

def pokaz_suma():
    data_szukana = input("Podaj date (rrrr-mm-dd): ")
    suma = 0
    if data_szukana in wydatki:
        for w in wydatki[data_szukana]:
            suma += w['kwota']
        print(f"Suma wydatków: {round(suma,2)} PLN")
    else:
        print("Nie ma takiej daty")

def zapis_do_pliku():
    with open("managerWydatkow.txt", "a", encoding="utf-8") as plik:
        for data, wartosc in wydatki.items():
            plik.write(f"{data}: \n")
            for w in wartosc:
                plik.write(f"- {w['nazwa']}, {w['kwota']} PLN, ({w['kategoria']})\n")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2:pokaz_wszystkie_wydatki, 3:pokaz_kategoria, 4:pokaz_suma, 5:zapis_do_pliku, 6:zakoncz}

print("=== MENU WYDATKOW ===\n 1.Dodaj wydatek\n 2. Pokaż wszystkie wydatki\n"
      "3. Pokaż tylko z kategorii\n 4. Pokaż sumę wydatków z dnia\n 5. Zapisz do pliku\n 6. Zakończ")

while(True):
    try:
        wybor = int(input("Podaj numer: "))
        funkcja = menu.get(wybor)
        if funkcja:
            funkcja()
        else:
            print("Nie ma takiej opcji")
    except ValueError:
        print("Niepoprawnie wprowadzona zmienna")