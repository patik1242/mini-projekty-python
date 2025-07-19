print("Automat z napojami")
napoje = {
    "Kawa": {
        "Espresso": 6.00,
        "Cappuccino": 8.50
    },
    "Herbata": {
        "Czarna": 5.00,
        "Zielona": 5.50
    },
    "Soki": {
        "Pomarańczowy": 7.00,
        "Jabłkowy": 6.50
    }
}

for (kategoria, rodzaj) in napoje.items():
    print(f"=={kategoria.upper()}==")
    for i,(pozycja, cena) in enumerate(rodzaj.items(), start = 1):
        print(f"{i}. {pozycja} - {cena} PLN")

zamowienie = {}

while(True):
    wybor1 = input("Wybierz kategorie, 0, aby zakonczyc: ").title()
    print(f"Wybrano {wybor1}")

    if(wybor1 == "0"):
        print("==RACHUNEK==")
        suma = 0
        for produkt, ilosc in zamowienie.items():
            for (kategoria, rodzaj) in napoje.items():
                if produkt in rodzaj:
                    cena = rodzaj[produkt]
                    break
            else:
                print(f"Nie znaleziono modelu {produkt} w liscie. Pomijam")
                continue
            koszt = cena * ilosc
            suma += koszt
            print(f"{ilosc}x {produkt} - {round(koszt,2)} PLN")
        print(f"Suma: {round(suma,2)}")


    wybor2 = int(input("Wybierz napoj: "))
    lista_napojow = list(napoje[wybor1].items())
    produkt = lista_napojow[wybor2-1][0]
    ilosc = int(input("Podaj ilosc: "))
    print(f"Dodano {produkt}")
    
    if produkt in zamowienie:
        zamowienie[produkt] += ilosc
    else:
        zamowienie[produkt] = ilosc