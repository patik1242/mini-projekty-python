print("Biblioteka - wypozyczalnia ksiazek")
biblioteka = {}
wypozyczone = {}
def dodaj():
    autor = input("Podaj autora: ").strip().title()
    tytul_ksiazki = input("Podaj tytul ksiazki: ")
    if autor in biblioteka:
        biblioteka[autor].append(tytul_ksiazki)
    else:
        biblioteka[autor] = [tytul_ksiazki]
    print(f"Dodano {tytul_ksiazki}")

def wypozycz():
    autor = input("Podaj autora: ").strip().title()
    wypozyczenie = input(f"Podaj tytul ksiazki do wypozyczenia: ")
    if wypozyczenie in biblioteka[autor] and autor in biblioteka:
        biblioteka[autor].remove(wypozyczenie)
        if autor in wypozyczone:
            wypozyczone[autor].append(wypozyczenie)
        else:
            wypozyczone[autor] = [wypozyczenie]
        print(f"Wypozyczono : {wypozyczenie}")
    else:
        print(f"Nie ma takiej ksiazki")

def zwroc():
    autor = input("Podaj autora: ").strip().title()
    zwrot = input(f"Podaj tytul ksiazki do zwrocenia: ")
    if autor in wypozyczone and zwrot in wypozyczone[autor]:
        wypozyczone[autor].remove(zwrot)
        if autor in biblioteka:
            biblioteka[autor].append(zwrot)
        else:
            biblioteka[autor] = [zwrot]
        print(f"Zwrocono {zwrot}")
    else:
        print(f"Nie znaleziono takiego wypozyczenia")

def pokaz():
    print("==DOSTEPNE KSIAZKI==")
    for (autor, tytul_ksiazki) in biblioteka.items():
        print(f"{autor} - {tytul_ksiazki}")

def pokaz_wypozyczone():
    print("==WYPOZYCZONE KSIAZKI==")
    for (autor, tytul_ksiazki) in wypozyczone.items():
        print(f"{autor} - {tytul_ksiazki}")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2:wypozycz, 3: zwroc, 4:pokaz, 5: pokaz_wypozyczone, 6: zakoncz}
print("==BIBLIOTEKA==\n 1. Dodaj ksiazke\n 2. Wypozycz ksiazke\n 3. Zwroc ksiazke\n4. Pokaz dostepne ksiazki\n5. Pokaz wypozyczone ksiazki\n 6. Zakoncz ")
while(True):
    wybor = int(input("Podaj numer: "))
    funkcja = menu.get(wybor)
    if(funkcja):
        funkcja()
    else:
        print("Nie ma takiej opcji")