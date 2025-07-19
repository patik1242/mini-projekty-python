print("Analiza Ocen")

oceny_str = input("Wprowadz swoje oceny oddzielone spacja: ").split()
oceny = []

for o in oceny_str:
    oceny.append(int(o))
    
    
liczba = len(oceny)
srednia = sum(oceny)/len(oceny)
max = max(oceny)
min = min(oceny)
ilosc = oceny.count(1)

print(f"Analiza ocen\n 1.Liczba ocen: {liczba}\n 2. Srednia ocen: {round(srednia,2)}\n"
      f"3.Najwyzsza ocena: {max}\n 4.Najnizsza ocena {min}\n 5. Ilosc jedynek: {ilosc}\n")