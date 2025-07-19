print("Kino")
filmy = {
    "Incepcja": 22.0,
    "Barbie": 19.5,
    "Oppenheimer": 25.0,
    "Avatar": 21.0,
    "Shrek 5": 18.0
}

lista_filmow = list(filmy.keys())
rezerwacje = {}

for i, element in enumerate(filmy, start = 1):
    print(f"{i}. {element} - {filmy.get(element)} PLN")

while(True):
    wybor = int(input("Wybierz numer z filmem, napisz 0, aby zakonczyc: "))
    if(wybor==0):
        print("==REZERWACJE==")
        suma = 0
        for film,bilet in rezerwacje.items():
            cena = filmy[film] * bilet
            suma += cena
            print(f"{bilet}x {film} - {round(cena,2)} PLN")
        print(f"Suma: {round(suma,2)} PLN")    
        break   
    if wybor>=1 and wybor<=len(lista_filmow):
        bilety = lista_filmow[wybor - 1]
        print(f"Wybrales: {bilety}")
        bilet = int(input("Ile chcesz biletow kupic: "))
        if bilety in rezerwacje:
            rezerwacje[bilety] +=bilet
        else:
            rezerwacje[bilety] = bilet
    else:
        print("Nie ma takiego filmu")
     
        


    