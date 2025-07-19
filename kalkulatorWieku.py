from datetime import date

print("Licznik wieku")

rok = int(input("Podaj swoj rok urodzenia: "))

wiek = date.today().year- rok

print(f"Masz: {wiek} lat")