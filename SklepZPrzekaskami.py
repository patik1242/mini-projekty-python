print("Sklep z przekaskami")

produkty = {
    "Chipsy": 6.0,
    "Czekolada": 4.5,
    "Orzeszki": 5.0,
    "Paluszki": 3.5,
    "Woda": 2.0
}

for i, element in enumerate(produkty, start = 1):
    print(f"{i}. {element} - {produkty.get(element)} pln")

produkty1 = []
lista_produktow = list(produkty.keys())
while(True):
    wybor = int(input("Wprowadz numer produktu, wybierz 0, aby zakonczyc: "))
    if(wybor==0):
        print("==LISTA PRODUKTOW==")
        suma = 0
        for i in set(produkty1):
            ilosc = produkty1.count(i)
            cena = ilosc * produkty[i]
            suma+=cena
            print(f"{ilosc}x {i} - {round(cena,2)} pln ")
        print(f"Suma Zakupow wynosi: {round(suma,2)} pln")
        break
    produkt = lista_produktow[wybor - 1]
    produkty1.append(produkt)
    print(f"Dodano {produkt}")

