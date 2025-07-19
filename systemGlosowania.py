print("system głosowania")

pomysly = {}

def dodaj_pomysl():
    nazwa = input("Podaj nazwe pomyslu: ").strip().title()
    glos = 0 
    if nazwa in pomysly:
        print("Taki pomysl juz istnieje")
    else:
        opis = input("Podaj opis: ")
        nowy = {"opis": opis, "glosy": glos}
        pomysly[nazwa] = nowy
        print("Pomysl zostal dodany")

def oddaj_glos():
    print("== Dostępne pomysły ==")
    for nazwa, wartosc in pomysly.items():
        print(f" - {nazwa}")
    nazwa = input("Na który pomysł chcesz oddac glos: ").strip().title()
    if nazwa in pomysly:
        pomysly[nazwa]['glosy'] +=1
    else:
        print("Nie ma takiego pomyslu")
    print("Dziękujemy za głos!")

def pokaz_ranking():
    print("=== RANKING POMYSLOW ===")
    for i, (nazwa, wartosc) in enumerate(sorted(pomysly.items(),key= lambda x: x[1]['glosy'], reverse = True), start= 1):
        print(f"{i}. {nazwa} - {pomysly[nazwa]['glosy']} głosów")

def zapis_do_pliku():
    with open("systemGlosowania.txt", "a", encoding="utf-8") as plik:
        for nazwa, wartosc in sorted(pomysly.items(), key= lambda x: x[1]['glosy'], reverse= True):
            plik.write(f"{nazwa} : {pomysly[nazwa]['glosy']} głosów - {pomysly[nazwa]['opis']}\n")
    print("Treść zapisana do systemGlosowania.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj_pomysl, 2:oddaj_glos, 3:pokaz_ranking, 4:zapis_do_pliku, 5:zakoncz}

print("=== SYSTEM GŁOSOWANIA ===\n 1. Dodaj pomysł\n 2. Oddaj głos\n 3. Pokaż ranking\n"
      "4. Zapisz do pliku\n 5. Zakończ")

while(True):
    try:
        wybor = int(input("Podaj numer: "))
        funkcja = menu.get(wybor)
        if funkcja:
            funkcja()
        else:
            print("Nie ma takiego numeru")
    except ValueError:
        print("Nie ma takiej opcji")
