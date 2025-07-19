print("Notatnik")
print("==MENU==\n 1. Dodaj notatkę\n 2. Pokaż notatki\n 3. Zakończ")


while(True):
    wybor = int(input("Wybierz numer: "))
    if(wybor ==1):
        notatka = input("Wpisz notatke: ")
        print(notatka)
        plik = open("notatki.txt", "a")
        plik.write(notatka + "\n")
        plik.close()
    elif(wybor==2):
        plik = open("notatki.txt", "r")
        for element in plik:
            print(element.strip())
        plik.close()
    elif(wybor==3):
        print("Zakonczono")
        break
    else:
        print("Nie ma takiej opcji w menu")
    






