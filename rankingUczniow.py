print("Ranking uczniow")

uczniowie = {}

def dodaj():
    imie = input("Podaj imie ucznia: ").strip().title()
    uczniowie[imie] = []
    print(f"Uczen {imie} dodany")

def ocena():
    imie = input("Podaj imie ucznia: ").strip().title()
    ocena = int(input("Podaj ocene: "))
    if imie in uczniowie:
        if(ocena>=1 and ocena<=6):
            uczniowie[imie].append(ocena)
        else:
            print("Nie ma takiej oceny")
    else:
        print("Nie ma takiego ucznia")

def pokaz():
    print("==RANKING==\n")
    for imie in uczniowie:
        oceny = uczniowie[imie]
        if (len(oceny)>0):
            srednia = sum(oceny)/len(oceny)
        print(f"-{imie} - średnia: {round(srednia,2)}")

def zapis():
    with open("ranking.txt", "w", encoding="utf-8") as plik:
        for imie in uczniowie:
            oceny = uczniowie[imie]
            if (len(oceny)>0):
                srednia = sum(oceny)/len(oceny)
            plik.write(f"{imie} - {uczniowie[imie]} - średnia: {round(srednia,2)}\n")
    print("Tresc zostala zapisana do ranking.txt")

def zakoncz():
    print("Zakonczono")
    exit()

print("==MENU RANKINGU==\n 1. Dodaj ucznia\n 2. Dodaj ocene\n 3. Pokaz ranking uczniow\n"
      "4. Zapisz do pliku\n 5. Wyjscie\n")

menu = {1: dodaj, 2: ocena, 3: pokaz, 4: zapis, 5: zakoncz}

while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    if funkcja:
        funkcja()
    else:
        print("Nie ma takiej opcji")