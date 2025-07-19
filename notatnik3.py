print("Notatnik")

notatnik = {}

def login():
    haslo = input("Podaj haslo: ").strip()

    if(haslo == "admin123"):
        print("Dostep przyznany")
        return True
    else:
        print("Nie przyznano dostepu")
        return False


def dodaj():
    tytul = input("Podaj tytuł notatki: ").strip().title()
    tresc = input("Podaj tresc notatki: ").strip().title()
    
    if tytul in notatnik:
        notatnik[tytul] +=" "+ tresc
    else:
        notatnik[tytul] = tresc
    
    print("Notatka dodana!")

def pokaz():
    for (tytul, tresc) in notatnik.items():
        print(f"- {tytul}: {tresc}\n")

def usun():
    tytul = input("Podaj tytul notatki do usuniecia: ").strip().title()
    if tytul in notatnik:
        del notatnik[tytul]
        print("Notatka zostala usunieta")
    else:
        print("Nie ma takiej notatki")

def zapis():
    with open("notatki3.txt", "w", encoding="utf-8") as plik:
        for tytul, tresc in notatnik.items():
            plik.write(f"{tytul} - {tresc}")
    print("Tresc zostala zapisana do pliku")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1:dodaj, 2:pokaz, 3: usun, 4:zapis, 5: zakoncz}

print("=== MENU NOTATNIKA ===\n 1. Dodaj notatkę\n 2. Pokaż notatki\n"
      "3. Usuń notatkę\n 4.Zapisz do pliku\n 5.Wyjście")

while(True):
    if login() == True:
        while(True):
            wybor = int(input("Wybierz numer: "))
            funkcja = menu.get(wybor)
            if funkcja:
                funkcja()
            else:
                print("Nie ma takiej opcji")
    else:
        wybor = input("Chcesz sprobowac ponownie? t/n: ")
        if(wybor == "t"):
            continue
        else:
            break
        

