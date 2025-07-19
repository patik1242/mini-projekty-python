print("Zarzadzanie uczestnikami na zawodach")

zawody = {}

def dodaj():
    nazwa_konkurencji = input("Podaj nazwe konkurencji: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko: ").strip().title()
    if nazwa_konkurencji not in zawody:
        zawody[nazwa_konkurencji] = {}
    if imie_i_nazwisko not in zawody[nazwa_konkurencji]:
        zawody[nazwa_konkurencji][imie_i_nazwisko] = []
        print(f"Uczestnik {imie_i_nazwisko} zostal dodany do {nazwa_konkurencji}")
    else:
        print("Uczestnik juz jest")

def wynik():
    nazwa_konkurencji = input("Podaj nazwe konkurencji: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko: ").strip().title()
    wynik = float(input("Podaj wynik: "))
    if nazwa_konkurencji in zawody and imie_i_nazwisko in zawody[nazwa_konkurencji]:
        zawody[nazwa_konkurencji][imie_i_nazwisko].append(wynik)
        print(f"{wynik} m zostal dodany do {imie_i_nazwisko}")
    else:
        print("Nie ma takiego uczestnika")

def wyswietl():
    nazwa_konkurencji = input("Podaj nazwe konkurencji: ").strip().title()
    if nazwa_konkurencji in zawody:
        print(f"Uczestnicy {nazwa_konkurencji}")
        for imie_i_nazwisko in zawody[nazwa_konkurencji]:
            print(f"-{imie_i_nazwisko}")

def sredni_wynik():
    nazwa_konkurencji = input("Podaj nazwe konkurencji: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko: ").strip().title()
    if nazwa_konkurencji in zawody and imie_i_nazwisko in zawody[nazwa_konkurencji]:
        wyniki = zawody[nazwa_konkurencji][imie_i_nazwisko]
        srednia = sum(wyniki)/len(wyniki)
        print(f"Srednia wynikow {imie_i_nazwisko} - {srednia}")
    else:
        print("Nie ma takiego uczestnika")

def zapis_do_pliku():
    with open("Zawody.txt", "w", encoding="utf-8") as plik:
        for nazwa_konkurencji, imie_i_nazwisko in zawody.items():
            plik.write(f"Uczestnicy {nazwa_konkurencji}\n")
            for osoba, wynik in imie_i_nazwisko.items():
                plik.write(f"- {osoba} - {wynik}\n")
    print("Dane zapisano do pliku Zawody.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2:wynik, 3:wyswietl, 4: sredni_wynik, 5:zapis_do_pliku, 6:zakoncz }
print("==MENU==\n 1. Dodaj uczestnika\n 2. Dodaj wynik\n 3. Wyswietl uczestnikow\n"
      "4. Sredni wynik\n 5.Zapisz do pliku\n 6. Zakoncz")

while(True):
    wybor = int(input("Podaj liczbe: "))
    funkcja = menu.get(wybor)
    if(funkcja):
        funkcja()
    else:
        print("Nie ma takiej opcji")
        