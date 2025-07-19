print("System obsługi klientów w sklepie")

klienci = {}

def dodaj():
    email = input("Podaj email: ")
    produkt = input("Podaj produkt: ")
    cena = float(input("Podaj cene: "))
    nowy = {"produkt": produkt, "cena": round(cena,2)}
    if email in klienci:
        klienci[email].append(nowy)
    else:
        klienci[email] = [nowy]
    
    print("Produkt dodany")

def historia_klienta():
    email = input("Podaj email: ")
    znaleziono = False
    if email in klienci:
        print("Zamówienie:")
        for w in klienci[email]:
            print(f"-{w['produkt']}: {w['cena']} PLN")
        znaleziono = True
    
    if not znaleziono:
        print("Nie ma takiego klienta w bazie")
                                    
def wszyscy_klienci():
    for email, wartosc in klienci.items():
        print(f"{email}: ")
        for w in wartosc:
            print(f"- {w['produkt']}: {w['cena']} PLN")

def suma_wydatkow():
    email = input("Podaj email: ")
    znaleziono = False
    suma = 0 
    if email in klienci:
        for w in klienci[email]:
            suma += w['cena']
        znaleziono = True
        print(f"Suma wydatków: {round(suma, 2)} PLN")
    
    if not znaleziono:
        print("Nie ma takiego klienta w bazie")

def zapis_do_pliku():
    with open("systemObslugi.txt", "a", encoding="utf-8") as plik:
        for email, wartosc in klienci.items():
            plik.write(f"{email}:\n")
            for w in wartosc:
                plik.write(f"-{w['produkt']}: {w['cena']} PLN\n")
    print("Zapisano do systemObslugi.txt")
    
def zakoncz():
    print("Zakonczono")
    exit()

menu = {1:dodaj, 2:historia_klienta, 3:wszyscy_klienci, 4:suma_wydatkow, 5:zapis_do_pliku, 6:zakoncz} 

print("=== SYSTEM OBSŁUGI KLIENTA ===\n 1. Dodaj zamówienie\n 2. Historia klienta\n 3. Wszyscy klienci\n 4. Suma wydatków klienta\n"
      "5. Zapisz do pliku\n 6. Wyjście")

while(True):
    try:
        wybor = int(input("Wybierz numer: "))
        funkcja = menu.get(wybor)
        if funkcja:
            funkcja()
        else:
            print("Nie ma takiego numeru")
    except ValueError:
        print("Nie ma takiej opcji")