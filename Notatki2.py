print("Notatnik")
print("==MENU==\n 1. Dodaj notatkę\n 2. Pokaż notatki\n 3. Zakończ")

def dodaj():
    plik = open("notatnik2.txt", "a")
    notatka = input("Wprowadz notatke: ")
    print(notatka)
    plik.write(notatka + "\n")
    plik.close()

def pokaz():
    plik = open("notatnik2.txt", "r")
    for element in plik:
        print(element.strip())
    plik.close()

def zakoncz():
    exit()

menu = {1: dodaj, 2:pokaz, 3:zakoncz}

while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    if funkcja:
        funkcja()
    else:
        print("Nie ma takiej opcji")