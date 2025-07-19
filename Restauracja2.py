print("Restauracja z kategoriami dań")
menu = {"Dania Główne": 
         {"Pizza Margherita": 26.0, "Spaghetti": 29.0,},
         "Zupy": {"Zupa pomidorowa": 15.5, "Rosół": 14.0,},
         "Desery": {"Sernik": 12.0, "Lody": 10.0,}}

zamowienie = {}
for kategoria, dania_w_kategorii in menu.items():
    print(f"=={kategoria.upper()}==")
    for i, (nazwa_dania, cena) in enumerate(dania_w_kategorii.items(), start =1):
        print(f"{i}. {nazwa_dania} - {cena} PLN")

while(True):
    wybor1 = input("Wybierz kategoria dania, wybierz 0, aby zakonczyc: ").title()
    print(f"Wybrano kategorie: {wybor1}")
    if(wybor1=="0"):
        print("==RACHUNEK==")
        suma = 0
        for (danie, ilosc) in zamowienie.items():
            for kategoria in menu.values():
                if danie in kategoria:
                    koszt = kategoria[danie]
                    break
            else:
                print(f"Nie znaleziono dania '{danie}' w menu. Pomijam.")
                continue
            cena = koszt * ilosc
            suma+=cena
            print(f"{ilosc}x {danie} - {round(cena,2)} PLN")
        print(f"Suma: {round(suma,2)}")
        break
    wybor2 = int(input("Wybierz pozycje: "))
    dania_w_kategorii = list(menu[wybor1].items())

    if(wybor2>=1 and len(dania_w_kategorii)):
        danie = dania_w_kategorii[wybor2-1][0]
    else:
        print("Nie ma takiej pozycji")
        continue

    print(f"Dodano: {danie}")
    ilosc = int(input("Podaj ilosc porcji: "))
    if danie in zamowienie:
        zamowienie[danie] += ilosc
    else:
        zamowienie[danie] = ilosc

    