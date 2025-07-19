def dodawanie(a,b):
    return a+b
def odejmowanie (a,b):
    return a-b
def mnozenie (a,b):
    return a*b
def dzielenie (a,b):
    return a/b

print("1.Dodawanie\n 2.Odejmowanie\n 3.Mnozenie\n 4.Dzielenie\n")

while True:
    a = float(input("Wybierz pierwsza liczbe: "))
    b = float(input("Wybierz druga liczbe: "))

    odp = int(input("Wybierz numerek, aby wybrac dzialanie: "))

    #zamiast if mozna uzywac match, case
    match(odp):
        case 1:
            wynik = dodawanie(a,b)
        case 2:
            wynik = odejmowanie(a,b)
        case 3:
            wynik = mnozenie(a,b)
        case 4:
            wynik = dzielenie(a,b)
        case _:
            #kiedy zostanie wprowadzona niepoprawna opcja
            raise ValueError("Nie ma takiej opcji")

    print(wynik)