print("Dziennik ucznia")
dziennik = {}

def dodaj():
    przedmiot = input("Podaj przedmiot: ").lower().strip()
    ocena = int(input("Wpisz ocene: "))
    if przedmiot.strip() in dziennik:
        dziennik[przedmiot].append(ocena)
    else:
        dziennik[przedmiot] = [ocena]
    print(f"Ocena {ocena} wpisana")
    

def pokaz():
    plik = open("DziennikOcen.txt", "a")
    for (przedmiot, ocena) in dziennik.items():
        print(f"{przedmiot} - {ocena}")
        plik.write(f"{przedmiot} - {ocena}\n")
    plik.close()

def srednia():
    przedmiotSrednia = input("Podaj z jakiego przedmiotu chcesz obliczyc srednia: ")
    if przedmiotSrednia in dziennik:
        liczba_ocen = len(dziennik[przedmiotSrednia])
        srednia = sum(dziennik[przedmiotSrednia])/liczba_ocen
        print(f"Srednia z przedmiotu: {round(srednia,2)}")
        plik = open("DziennikOcen.txt", "a")
        plik.write(f"{przedmiotSrednia} - {srednia}\n")
        plik.close()
    else:
        print("Nie ma takiego przedmiotu")
        
def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2:pokaz, 3:srednia, 4: zakoncz}
print("==DZIENNIK==\n 1. Dodaj ocene\n 2.Pokaz oceny\n 3. Oblicz srednia\n 4. Zakoncz\n")
while(True):
    wybor = int(input("Podaj numer: "))
    funkcja = menu.get(wybor)
    if(funkcja):
        funkcja()
    else:
        print("Nie ma takiej opcji")