print("Srednia ocen")

print("Wpisuj oceny, jak bedzie koniec to napisz 'koniec' ")
oceny = []

while(True):
    oceny_str = input("Podaj ocenę: ") #oceny sa podawane w formie stringow
    if(oceny_str.lower() == "koniec"):
        break
    else:
        ocena = int(oceny_str)
        if(ocena>=1 and ocena<=6):
            oceny.append(ocena)
        else:
            print("Nie ma takiej oceny")

if(oceny):
    srednia = sum(oceny)/len(oceny)
    print(f"Twoja srednia to: {round(srednia,2)}")
else:
    print("Nie podano zadnych ocen")
