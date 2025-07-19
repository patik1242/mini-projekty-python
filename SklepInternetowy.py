print("Sklep internetowy z koszykiem")
produkty = {
    "Laptop": {"cena": 3000, "kategoria": "Elektronika"},
    "Myszka": {"cena": 80, "kategoria": "Elektronika"},
    "Książka": {"cena": 40, "kategoria": "Kultura"},
    "Bluza": {"cena": 120, "kategoria": "Odzież"}
}
koszyk = {}

def wszystkie_produkty():
    print("== Produkty w sklepie ==")
    for produkt, cena in produkty.items():
        print(f"- {produkt}: ", end = " ")
        for koszt, kat in cena.items():
            if koszt=="cena":
                print(f"{kat} PLN", end = " ")
            elif koszt=="kategoria":
                print(f"({kat})", end = " ")
        print(" ")

def pokaz_kategoria():
    kategoria = input("Podaj kategorie: ").strip().title()
    znaleziono = False
    for produkt, cena in produkty.items():
        if cena['kategoria'] == kategoria:
            print(f"- {produkt} - {cena['cena']} PLN")
            znaleziono = True
    
    if not znaleziono:
        print("Nie ma takiej kategorii")

def dodaj_produkt():
    produkt = input("Podaj nazwe produktu: ").strip().title()
    if produkt in produkty:
        if produkt in koszyk:
            koszyk[produkt] += 1
        else:
            koszyk[produkt] = 1
        print(f"{produkt} dodany do koszyka")
    else:
        print("Nie ma takiego produktu")
    
def pokaz_koszyk():
    suma = 0 
    for nazwa, ilosc in koszyk.items():
        cena = produkty[nazwa]['cena']
        print(f"{nazwa} x{ilosc} - {cena*ilosc} PLN")
        suma += cena*ilosc
    print(f"suma: {suma}")

def zapis_do_pliku():
    with open("koszyk.txt", "w", encoding="utf-8") as plik:
        plik.write("==Zamowienie==\n")
        suma = 0 
        for nazwa, ilosc in koszyk.items():
            cena = produkty[nazwa]['cena']
            plik.write(f"{nazwa} x{ilosc} - {cena*ilosc} PLN\n")
            suma += cena*ilosc
        plik.write(f"suma: {suma}")
    print("Zapisano do koszyk.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: wszystkie_produkty, 2: pokaz_kategoria, 3: dodaj_produkt, 4: pokaz_koszyk, 5:zapis_do_pliku, 6:zakoncz}

print("==MENU SKLEPU==\n 1.Pokaż wszystkie produkty\n 2.Pokaż tylko z kategorii\n 3.Dodaj produkt do koszyka\n"
      "4. Pokaż koszyk\n 5.Zapisz zamówienie\n 6. Zakończ")


while(True):
    wybor = int(input("Podaj numer: "))
    funkcja = menu.get(wybor)
    if funkcja:
        funkcja()
    else:
        print("Nie ma takiej opcji")