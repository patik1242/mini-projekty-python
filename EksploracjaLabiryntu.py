print("Eksploracja labiryntu")

mapa = {
    (0, 0): {"opis": "Start – ciemny pokój", "przedmiot": None},
    (0, 1): {"opis": "Znalazłeś klucz!", "przedmiot": "klucz"},
    (1, 1): {"opis": "Pokój z pułapką", "przedmiot": None},
    (2, 2): {"opis": "Skarbiec!", "przedmiot": "skarb"}
}

gracz = {
    "pozycja": (0, 0),
    "ekwipunek": [],
    "punkty": 0
}

def ruch():
    ruch = input("W którą stronę? (prawo/lewo/góra/dół) ")
    x, y = gracz['pozycja']
    if ruch == "prawo":
        y+=1
    elif ruch == "lewo":
        y-=1
    elif ruch == "góra":
        x+=1
    elif ruch == "dół":
        x-=1
    else:
        print("Nie ma takiego kierunku")

    gracz['pozycja'] = (x,y)
    print(f"Przesunięto na {gracz['pozycja']}")
    
    
def sprawdz_pole():
    znaleziono = False
    for polozenie, wartosc in mapa.items():
        if gracz['pozycja'] == polozenie:
            print(f"Opis pola: {mapa[polozenie]['opis']}")
            if mapa[polozenie]['przedmiot'] == None:
                print("Na tym polu nie ma żadnego przedmiotu")
            else:
                print(f"Na polu znajduje się {mapa[polozenie]['przedmiot']}")
            znaleziono = True
    
    if not znaleziono:
        print("Pole puste")
        

def podnies_przedmiot():
    znaleziono = False
    for polozenie, wartosc in mapa.items():
        if gracz['pozycja'] == polozenie:
            if mapa[polozenie]['przedmiot'] == None:
                print("Na polu, którym się znajdujesz nie ma przedmiotu, którego możesz podnieść")
            else:
                print(f"Podnosisz przedmiot: {mapa[polozenie]['przedmiot']}")
                gracz["punkty"] +=10
                gracz['ekwipunek'].append(mapa[polozenie]['przedmiot'])
                znaleziono = True
                if mapa[polozenie]['przedmiot'] == "skarb":
                    print("Podniosłeś SKARB! Wygrałeś grę!")
                    exit()
                mapa[polozenie]['przedmiot'] = None
    if not znaleziono:
        print("Nie ma żadnego przedmiotu do podniesienia")
    
def ekwipunek():
    if gracz['ekwipunek'] == []:
        print("Nic nie masz")
    else:
        print("== Ekwipunek ==")
        for przedmiot in gracz["ekwipunek"]:
            print(f" - {przedmiot}")
def zapisz_postep():
    with open("EksploracjaLabiryntu.txt", "w", encoding="utf-8") as plik:
        plik.write(f"Pozycja: {gracz['pozycja']}\n Ekwipunek: {gracz['ekwipunek']}\n"
            f"Punkty: {gracz['punkty']}\n")
    print("Zapisano do EksploracjaLabiryntu.txt") 

def zakoncz():
    print("Zakonczono")
    exit()         

menu = {1: ruch, 2:sprawdz_pole, 3:podnies_przedmiot, 4:ekwipunek, 5:zapisz_postep, 6:zakoncz}

print("=== EKSPLORACJA LABIRYNTU ===\n 1. Ruch\n 2. Sprawdź pole\n 3. Podnieś przedmiot\n"
      "4. Ekwipunek\n 5. Zapisz postęp\n 6. Wyjście")

while(True):
    try:
        wybor = int(input("Podaj numer: "))
        funkcja = menu.get(wybor)
        if funkcja:
            funkcja()
        else:
            print("Nie ma takiej opcji")
    except ValueError:
        print("Nie można")


