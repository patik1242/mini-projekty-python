import random 

gracz = {"nick": "Hero", "hp": 100}
potwor = {"nazwa": "Goblin", "hp": 60}

def atakuj():
    obrazenia_gracz = random.randrange(0,20)
    obrazenia_potwor = random.randrange(0,20)
    gracz['hp'] -= obrazenia_potwor
    potwor['hp'] -= obrazenia_gracz
    print(f"\nZadajesz {obrazenia_gracz} obrażeń")
    
    if(potwor['hp']<=0):
        print("Goblin pokonany!")
        with open("rankingGra.txt", "a", encoding = "utf-8") as plik:
            plik.write(f"{imie} - wygral w walce z goblinem - hp: {gracz['hp']} \n")

    elif(gracz['hp']<=0):
        print("Przegrales")
        with open("rankingGra.txt", "a", encoding = "utf-8") as plik:
            plik.write(f"{imie} - przegral w walce z goblinem \n")
    else:
        print(f"Goblin zadaje {obrazenia_potwor} obrażeń\n")
        print(f"Twoje Hp: {gracz['hp']} | Goblin Hp: {potwor['hp']}\n")

def leczSie():
    leczenie_gracz = random.randrange(0,20)
    obrazenia_potwor = random.randrange(0,20)
    gracz['hp'] += leczenie_gracz
    gracz['hp'] -= obrazenia_potwor
    print(f"\nLeczysz sie o {leczenie_gracz} hP \n Goblin zadaje {obrazenia_potwor} obrażeń\n")
    if gracz['hp']>100:
        gracz['hp'] = 100
    if(gracz['hp']<=0):
        print("Przegrales")
        with open("rankingGra.txt", "a", encoding = "utf-8") as plik:
            plik.write(f"{imie} - przegral w walce z goblinem \n")
    else:
        print(f"Twoje Hp: {gracz['hp']} | Goblin Hp: {potwor['hp']}\n")

def ucieczka():
    print("Zakonczenie gry\n")  
    print(f"Twoje Hp: {gracz['hp']} | Goblin Hp: {potwor['hp']}\n")

    with open("rankingGra.txt", "a", encoding = "utf-8") as plik:
        plik.write(f"{imie} - uciekla \n")

    exit()

menu = {1:atakuj, 2:leczSie, 3:ucieczka}

print("Witaj w grze RPG!")
imie = input("Podaj imie bohatera: ")

print(f"Twoje hp: {gracz['hp']} | Goblin Hp: {potwor['hp']}\n")
print("==MENU==\n 1. Atakuj\n 2. Lecz sie\n 3. Ucieczka")

while(True):
    if(gracz['hp'] <=0 or potwor['hp']<=0):
         print("=== KONIEC GRY ===")
         break
    elif(gracz['hp']>0):
        try:
            wybor = int(input("Co chcesz zrobic? "))
            funkcja = menu.get(wybor)
            if funkcja:
                funkcja()
            else:
                print("Nie ma takiej opcji")
        except ValueError:
            print("Wpisz poprawny numer opcji!")
