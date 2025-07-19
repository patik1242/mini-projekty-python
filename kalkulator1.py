#jak się robi funkcje
def dodawanie(a,b):
    return a +b
def odejmowanie(a,b):
    return a-b
def mnozenie(a,b):
    return a*b
def dzielenie(a,b):
    return a/b

#\n --> nowa linijka
print("\n1. Dodawanie\n 2. Odejmowanie\n 3. Mnozenie\n 4. Dzielenie\n")

#True - petla nieskonczona
while True:
    #input - uzytkownik moze wprowadzic liczbe
    odp = int(input("Wybierz cyfre odpowiadajaca dzialaniu: "))

    #if, zamiast else if to elif, a else to else
    if (odp>=1 and odp<=4):
        a = float(input("Wprowadz pierwsza liczbe: ")) #float - zmiennoprzecinkowe, uzytkownik moze wprowadzac liczby zmiennoprzecinkowe
        b = float(input("Wprowadz druga liczbe: "))
        if(odp==1):
            wynik = dodawanie(a,b)
        elif(odp==2):
            wynik = odejmowanie(a,b)
        elif(odp==3):
            wynik = mnozenie(a,b)
        elif(odp==4):
            wynik = dzielenie(a,b)

        print(wynik)
    else:
        print("Nie ma takiej liczby do wyboru")
    

