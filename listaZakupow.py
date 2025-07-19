print("Lista zakupow")
zakupy = []
print("1. Dodaj produkt\n 2. Usuń produkt\n 3. Pokaż listę zakupów\n 4.Zakończ")
while(True):
    opcja = int(input("Wybierz numerek: "))
    if(opcja == 1):
        produkt = input("Podaj nazwe produktu: ")
        zakupy.append(produkt)
        print(f"Dodano {produkt} do listy")
    elif(opcja ==2):
        produkt2 = input("Podaj produkt do usuniecia: ")
        if(produkt2 in zakupy):
            zakupy.remove(produkt2)
            print(f"Usunieto {produkt2} z listy")
        else:
            print("Nie ma takiego produktu w liscie")
    elif(opcja ==3):
        for element in zakupy:
            print(element)
    elif(opcja ==4):
        break
    else:
        print("Nie ma takiej opcji w menu")

    

