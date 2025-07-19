print("Analiza ocen")

oceny = []

while(True):
    wpis = input("Podaj ocene, jesli koniec to wpisz 'koniec': ")
    if(wpis.lower() == "koniec"):
        break
    else:
        ocena = int(wpis)
        if(ocena>=1 and ocena<=6):
            oceny.append(ocena)
    
liczba = len(oceny)
srednia = sum(oceny)/len(oceny)
max = max(oceny)
min = min(oceny)
ilosc1 = oceny.count(1)

print(f"1.Liczba ocen: {liczba}\n 2.Srednia ocen: {round(srednia,2)} 3.Najwyzsza ocena: {max} "
      f"4. Najnizsza ocena: {min}\n 5.Ilosc jedynek: {ilosc1}")