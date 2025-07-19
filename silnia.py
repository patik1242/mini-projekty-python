print("OBLICZANIE SILNI")

liczba = int(input("Podaj liczbe: "))
wynik = 1

for i in range(1,liczba+1):
    wynik *= i

print(f"{liczba}! = {wynik}")
