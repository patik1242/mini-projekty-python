print("Średnia ocen z listy")

oceny_str = input("Wprowadz swoje oceny oddzielone spacja: ").split() #zapisuje w formie str
#oceny = [int(o) for o in oceny] 
#konwertuje każdy str na int

oceny = []

for o in oceny_str:
    oceny.append(int(o))

if(oceny):
    srednia = sum(oceny)/len(oceny)
    print(f"Srednia ocen: {round(srednia,2)}")
else:
    print("Nie podano zadnych ocen")
