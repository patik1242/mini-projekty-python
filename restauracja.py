print("Restauracja")
menu = {
    "Pizza Margherita": 26.0,
    "Spaghetti Bolognese": 29.0,
    "Zupa Pomidorowa": 15.5,
    "Sałatka Grecka": 19.0,
    "Sernik": 12.0
}

lista_menu = list(menu.keys())

zamowienie = {}

print("==MENU==")
for i, element in enumerate(menu, start = 1):
    print(f"{i}. {element} - {menu.get(element)} PLN")

while(True):
    wybor = int(input("Wybierz numer dania, 0, aby zakonczyc: "))
    if(wybor ==0):
        print("==ZAMOWIENIE==")
        suma = 0
        for danie,ile in zamowienie.items():
            cena = menu[danie] * ile
            suma += cena
            print(f"{ile}x {danie} - {round(cena,2)} PLN")
        print(f"Suma: {round(suma,2)}")
        break
    danie = lista_menu[wybor-1]
    print(f"Dodano: {danie}")
    ile = int(input("Ile porcji: "))
    if danie in zamowienie:
        zamowienie[danie] += ile  
    else:
        zamowienie[danie] = ile 

