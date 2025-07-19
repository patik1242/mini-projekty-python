print("System oceniania")
print("Witaj w tescie!")
odpowiedzi = input("Podaj swoje odpowiedzi np.ABCDA: ").upper()
poprawne_odpowiedzi = ["A", "B", "A", "C", "D"]
odpowiedzi_lista = list(odpowiedzi)

if(len(odpowiedzi_lista)!= len(poprawne_odpowiedzi)):
    print("Podales bledna liczbe odpowiedzi")

poprawne_licznik = 0

for i in range(len(poprawne_odpowiedzi)):
    if(odpowiedzi_lista[i]==poprawne_odpowiedzi[i]):
        poprawne_licznik+=1

procent = poprawne_licznik/len(poprawne_odpowiedzi) *100

print(f"Poprawnych odpowiedzi: {poprawne_licznik}/5")
print(f"Wynik: {round(procent,2)} %")

if(procent>=50):
    print("ZDANE!")
else:
    print("Niezdane")