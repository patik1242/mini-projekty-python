import math

def czyPierwsza(n):
    if n<2:
        return False
    #for i in range(2, (sqrt(n)+1)) 
    for i in range(2, n):
        if n%i == 0:
            return False
    return True


print("Sprawdzanie czy liczba jest pierwsza")

liczba = int(input("Wprowadz liczbe: "))

if czyPierwsza(liczba) == True:
    print("Jest to liczba pierwsza")
    for i in range(2,101):
        if(czyPierwsza(i)):
            print(i, end = " ")
            
else:
    print("Nie jest")

