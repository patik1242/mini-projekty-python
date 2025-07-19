print("Sklep z elektronika")
asortyment = {
    "Laptopy": {
        "Dell XPS 13": 5299.99,
        "MacBook Air M2": 6499.00
    },
    "Smartfony": {
        "iPhone 13": 4199.00,
        "Samsung Galaxy S22": 3999.00
    },
    "Akcesoria": {
        "Słuchawki Sony WH-1000XM5": 1399.99,
        "Powerbank 20000mAh": 199.90
    }
}

zamowienie = {}

for kategoria, model in asortyment.items():
    print(f"=={kategoria.upper()}==")
    for i, (nazwa, cena) in enumerate(model.items(), start = 1):
        print(f"{i}.{nazwa} - {cena} PLN")

while(True):
    wybor1 = input("Wybierz kategorie, napisz 0, aby zakonczyc: ").title()
    print(f"Wybrano kategorie {wybor1}")
    
    if(wybor1 == "0"):
        print("==RACHUNEK==")
        suma = 0
        for (produkt, ilosc) in zamowienie.items():
            for kategoria, model in asortyment.items():
                if produkt in model:
                    cena = model[produkt]
                    break
            else:
                print(f"Nie znaleziono modelu {produkt} w liscie. Pomijam")
                continue
            koszt = cena * ilosc
            suma += koszt
            print(f"{ilosc}x {produkt} - {round(koszt,2)} PLN")
        print(f"Suma: {round(suma,2)} PLN")
        break


    wybor2 = int(input("Wybierz numer produktu: "))
    produkt_lista = list(asortyment[wybor1].items())
    produkt = produkt_lista[wybor2-1][0]
    print(f"Dodano {produkt}")
    ilosc = int(input("Podaj liczbe sztuk: "))
    if produkt in zamowienie:
        zamowienie[produkt] += ilosc
    else:
        zamowienie[produkt] = ilosc

