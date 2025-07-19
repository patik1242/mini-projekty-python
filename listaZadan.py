print("To-Do lista\n")

planer = {}

def dodaj():
    data = input("Podaj date (rrrr-mm-dd): ")
    zadanie = input("Zadanie: ").strip().title()
    priorytet = int(input("Priorytet: "))
    nowy = {"zadanie": zadanie, "priorytet" : priorytet}
    if data in planer:
        planer[data].append(nowy)
    else:
        planer[data] = [nowy]
    print("Dodano zadanie")

def pokaz_wszystkie_notatki():
    for data, wartosc in sorted(planer.items()):
        print(f"\n{data}:")
        for w in sorted(wartosc, key = lambda x: x['priorytet']):
            print(f"[{w['priorytet']}] {w['zadanie']}")
            
def pokaz_dzien():
    data = input("Podaj date (rrrr-mm-dd): ")
    znaleziono = False
    if data in planer:
        print("Zadania: ")
        for zadania in sorted(planer[data], key = lambda x: x['priorytet']):
            print(f"[{zadania['priorytet']}] - {zadania['zadanie']}")
        znaleziono = True

    if not znaleziono:
        print("Nie ma takiej daty")

def usun_zadanie():
    data = input("Podaj date (rrrr-mm-dd): ")
    znaleziono = False
    if data in planer:
        notatka = input("Podaj dokladna tresc notatki: ").strip().title()
        for w in planer[data]:
            if notatka == w['zadanie']:
                planer[data].remove(w)
                print("usunieto notatke")
                break
        else:
            print("nie ma takiej notatki")
        znaleziono = True

    if not znaleziono:
        print("Nie ma takiej daty")

def zapis_do_pliku():
    with open("listaZadan.txt", "a", encoding="utf-8") as plik:
        for data, wartosc in sorted(planer.items()):
            plik.write(f"{data}: \n")
            for w in sorted(wartosc, key = lambda x: x['priorytet']):
                plik.write(f"[{w['priorytet']}] - {w['zadanie']}\n")
    print("Zapisano do listaZadan.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2:pokaz_wszystkie_notatki, 3:pokaz_dzien, 4:usun_zadanie, 5:zapis_do_pliku, 6:zakoncz}
    
print("=== PLANER ZADAŃ ===\n 1. Dodaj zadanie\n 2. Pokaż wszystkie notatki\n 3. Pokaż z danego dnia\n"
      "4. Usuń zadanie\n 5. Zapisz do pliku\n 6. Zakończ\n")

while(True):
    try:
        wybor = int(input("Podaj numer: "))
        funkcja = menu.get(wybor)
        if funkcja:
            funkcja()
        else:
            print("Nie ma takiego numeru")
    except ValueError:
        print("Nieprawidlowo wprowadzone")


