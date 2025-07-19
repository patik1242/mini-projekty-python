print("Zamowienia w kawiarnii")
print("==MENU==\n")
menu = {"Espresso": 9.0, "Latte": 12.0, "Cappuccino": 11.5, "Herbata": 8.0}
lista_napojow = list(menu.keys())

for i, element in enumerate(menu, start = 1):
    print(f"{i}. {element} {menu.get(element)} pln")

napoje = []

while(True):
    wybor = int(input("Wprowadz numer napoju albo nacisnij 0 w celu zakonczenia: "))
    if(wybor == 0):
        print("==TWOJE ZAMOWIENIE==")
        suma = 0
        for i in set(napoje):
            ilosc = napoje.count(i)
            cena = ilosc*menu[i]
            print(f"{ilosc} {i} - {round(cena,2)} pln")
            suma+=cena
        print(f"Suma do zaplaty: {round(suma, 2)} pln ")
        break
    napoj = lista_napojow[wybor -1]
    napoje.append(napoj)
    print(f"Dodano: {napoj}")
    
