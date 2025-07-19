print("Przelicznik walut")

print("Dostepne waluty: USD, EUR, GBP, PLN\n Jesli chcesz zakonczyc napisz 'koniec'")

kursy = {"USD": 4.0, "EUR": 4.5, "GBP": 5.2, "PLN": 1.0}

def przelicz(waluta1, waluta2, kwota):
   
    if(waluta1 in kursy and waluta2 in kursy):
        kwota_PLN = kwota*(kursy.get(waluta1))
        przeliczona = kwota_PLN/(kursy.get(waluta2)) 

        print(f"{kwota} {waluta1} = {round(przeliczona,2)} {waluta2}")
    else:
        print("Waluta nieznana. Sprawdz czy sie znajduje w menu")

while(True):
    waluta1 = input("Z jakiej waluty chcesz przeliczyc?: ")
    if(waluta1 == "koniec"):
        break
    waluta2 = input("Na jaka walute?: ")
    kwota = float(input("Podaj kwote: "))
    przelicz(waluta1,waluta2,kwota)
    

        