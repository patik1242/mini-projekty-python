print("Dziennik")

dziennik = {}

def dodaj():
    imie = input("Wprowadz imie: ")
    ocena = input("Wprowadz ocene: ")
    dziennik[imie] = ocena
    print(f"Dodano {imie} : {ocena}")

def usun():
    imie = input("Wprowadz imie: ")
    if(imie in dziennik):
        del dziennik[imie]
        print(f"Usunieto {imie}")
    else:
        print("Nie ma takiej osoby")

def zmianaOceny():
    imie = input("Wprowadz imie: ")
    if(imie in dziennik):
        nowa_ocena = int(input("Wprowadz nowa ocene: "))
        dziennik[imie] = nowa_ocena
        print(f"Zmieniono {imie} ocene na: {nowa_ocena}")
    else:
        print("Nie ma takiej osoby")

def wyswietlanie():
    for imie in dziennik:
        print(f"{imie} : {dziennik[imie]}")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2: usun, 3: zmianaOceny, 4:wyswietlanie, 5: zakoncz}
print("1.Dodaj ucznia\n 2. Usuń ucznia\n 3.Zmień ocenę uczniowi\n 4.Wyświetl dziennik\n 5. Zakończ\n")

while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    funkcja()
