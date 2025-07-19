def bmi(wzrost, waga):
    wynik = (waga/((wzrost/100.0)**2))
    #print(f"Twoje bmi wynosi: {wynik:.2f}") 
    print(f"Twoje bmi wynosi: {round(wynik,2)} ") #Formatowanie zamiast setprecision<3333
    #print(round(wynik,2)) 

    if(wynik<17.0):
        print("Wychudzenie")
    elif(wynik>=17.0 and wynik<=18.4):
        print("Niedowaga")
    elif(wynik>18.4 and wynik<=24.9):
        print("Waga prawidlowa")
    elif(wynik>24.9 and wynik<=29.99):
        print("Nadwaga")
    else:
        print("Otylosc")

print("KALKULATOR BMI")

wzrost = float(input("Podaj swoj wzrost w centymetrach: "))
waga = float(input("Podaj swoja wage wyrazona w kg: "))


bmi(wzrost, waga)

