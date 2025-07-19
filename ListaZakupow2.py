print("Lista zakupow")

zakupy = []

def dodaj():
    produkt = input("Podaj nazwe produktu: ")
    zakupy.append(produkt)
    print(f"Dodano {produkt}")

def usun():
    produkt = input("Podaj nazwe produktu, ktory chcesz usunac: ")
    if(produkt in zakupy):
        zakupy.remove(produkt)
        print(f"Usunieto {produkt}")
    else:
        print("Nie ma takiego produktu")

def pokaz():
    for element in zakupy:
        print(element)
    
def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2: usun, 3: pokaz, 4: zakoncz}

print("1. Dodaj produkt\n 2. Usuń produkt\n 3. Pokaż listę zakupów\n 4.Zakończ")

while(True):
    wybor = int(input("Wprowadz numer: "))
    funkcja = menu.get(wybor)
    funkcja()
