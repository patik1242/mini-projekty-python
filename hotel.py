print("Rezerwacje w hotelu")
hotele = {
    "101": {"typ": "Jednoosobowy", "zajety": False},
    "102": {"typ": "Jednoosobowy", "zajety": True},
    "201": {"typ": "Dwuosobowy", "zajety": False},
    "202": {"typ": "Dwuosobowy", "zajety": False}
}

rezerwacje = []

def pokaz():
    print("Dostępne pokoje: ")
    for numer, pokoj in hotele.items():
        if pokoj['zajety'] == False:
            print(f"-{numer} - {pokoj['typ']}")
       # for rodzaj, wartosc in pokoj.items():
        #    if rodzaj == "typ":
         #       print(f"- {numer} - {wartosc}")

def rezerwacja():
    numer = input("Podaj numer pokoju: ")
    if numer in hotele:
        if hotele[numer]['zajety'] == False:
            hotele[numer]['zajety'] = True
            rezerwacje.append(numer)
            print(f"Pokój {numer} zostal zarezerwowany")
        else:
            print("Pokoj juz jest zajety")
    else:
        print("Nie ma takiego numeru")

def anulowanie():
    numer = input("Podaj numer pokoju: ")
    if numer in hotele:
        if hotele[numer]['zajety'] == True:
            hotele[numer]['zajety'] = False
            print(f"Anulowano rezerwacje pokoju {numer}")
        else:
            print("Pokoj juz byl wolny")
    else:
        print("Nie ma takiego pokoju")

def pokaz_rezerwacje():
    print("=== TWOJE REZERWACJE ==")
    for numer in rezerwacje:
        print(f"{numer} zarezerwowany")

def zapis_do_pliku():
    with open("hotel.txt", "w", encoding="utf-8") as plik:
        plik.write("=== POKOJE ===\n")
        for numer, pokoj in hotele.items():
            if pokoj['zajety'] == True:
                status = "zajęty"
            else:
                status = "wolny"
            plik.write(f"-{numer}: {pokoj['typ']} - {status}\n")
    print("Tresc zapisana do hotel.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1:pokaz, 2:rezerwacja, 3: anulowanie, 4: pokaz_rezerwacje, 5:zapis_do_pliku, 6:zakoncz}

print("=== MENU HOTELU ===\n 1. Pokaż dostępne pokoje\n 2. Zarezerwuj pokój\n"
      "3. Anuluj rezerwację\n 4. Pokaż twoje rezerwacje\n 5. Zapisz do pliku\n 6. Wyjście\n")

while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    if funkcja:
        funkcja()
    else:
        print("Nie ma takiej opcji")
