print("Kino")
filmy = {
    "Incepcja": {
        "18:00": {
            "A1": "wolne", "A2": "zajęte", "A3": "wolne",
            "B1": "zajęte", "B2": "wolne", "B3": "wolne"
        },
        "20:30": {
            "A1": "wolne", "A2": "wolne", "A3": "zajęte"
        }
    },
    "Shrek": {
        "17:00": {
            "A1": "zajęte", "A2": "zajęte", "A3": "wolne"
        }
    }
}
rezerwacje = {}
def pokaz():
    print("\n==FILMY==")
    for (tytul, godzina) in filmy.items():
        print(f"- {tytul}:",end = " ")
        for (czas, miejsce) in godzina.items():
            print(f"{czas}", end = " ")
        print("\n")
                
def rezerwacja():
    tytul = input("Podaj tytul filmu: ").strip().title()
    godzina = input("Podaj godzine seansu: (wpisz pelna godzine)").strip()
    
    if(tytul in filmy and godzina in filmy[tytul]):
        print("Dostepne miejsca: ")
        miejsca = filmy[tytul][godzina]
        for pozycja, status in miejsca.items():
            if status == "wolne":
                print(f"{pozycja}", end = " ")
        wybor_miejsca = input("Wybierz miejsce: ").strip().upper()
        if wybor_miejsca in miejsca and miejsca[wybor_miejsca] == "wolne":
            filmy[tytul][godzina][wybor_miejsca] = "zajęte"
            print(f"Wybrano: {wybor_miejsca}" )

            if tytul not in rezerwacje:
                rezerwacje[tytul] = {}
        
            if godzina not in rezerwacje[tytul]:
                rezerwacje[tytul][godzina] = []
            rezerwacje[tytul][godzina].append(wybor_miejsca)
        else:
            print("Nie ma takiego miejsca")
       
    else:
        print("Nie ma takiego seansu")

def wyswietl():
    tytul = input("Podaj tytul filmu: ").strip().title()
    godzina = input("Podaj godzine seansu: (wpisz pelna godzine)").strip()
    if tytul in filmy and godzina in filmy[tytul]:
        miejsca = filmy[tytul][godzina]
        print("Zajęte miejsca: ")
        for pozycja, status in miejsca.items():
            if status == "zajęte":
                print(f"{pozycja}", end = " ")
    else:
        print("Nie ma takiego seansu")
    
def zapis_do_pliku():
    with open("Kino.txt", "a", encoding="utf-8") as plik:
        for tytul, godziny in rezerwacje.items():
            for czas, miejsca in godziny.items():
                for pozycja in miejsca:
                    plik.write(f"{tytul} | {czas} | Miejsce: {pozycja}\n")
    print("Rezerwacje zapisane do pliku Kino.txt.")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: pokaz, 2:rezerwacja, 3: wyswietl, 4: zapis_do_pliku, 5: zakoncz}

print("==MENU KINA==\n 1.Pokaz dostepne filmy\n 2. Zarezerwuj miejsce\n 3. Zobacz rezerwacje\n"
      "4. Zapisz do pliku\n 5. Wyjscie")

while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    if funkcja:
        funkcja()
    else:
        print("Nie ma takiej opcji")
