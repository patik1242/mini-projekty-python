print("Dziennik")
print("1.Dodaj ucznia\n 2. Usuń ucznia\n 3.Zmień ocenę uczniowi\n 4.Wyświetl dziennik\n 5. Zakończ\n")
dziennik = {}
while(True):
    opcja = int(input("Wybierz numer: "))
    if(opcja==1):
        imie = input("Imie: ")
        ocena = input("Ocena: ")
        dziennik[imie] = ocena
        print(f"Dodano: {imie} : {ocena}")
    elif(opcja ==2):
        imie = input("Podaj imie: ")
        if(imie in dziennik):
            del dziennik[imie]
            print(f"Usunieto {imie}")
        else:
            print("Nie ma takiej osoby")
    elif(opcja==3):
        imie = input("Podaj imie: ")
        if(imie in dziennik):
            print(ocena)
            nowa_ocena = int(input("Wprowadz nowa ocene: "))
            dziennik[imie] = nowa_ocena
        else:
            print("Nie ma takiej osoby")
    elif(opcja==4):
        for imie in dziennik:
            print(imie, dziennik[imie])
    elif(opcja==5):
        print("Zakonczono")
        break
    else:
        print("Nie ma takiej opcji w mnenu")





