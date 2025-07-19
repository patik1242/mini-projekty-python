print("Licznik liter i cyfr w napisie")

napis = input("Wprowadz tekst: ")

licznik_liter = 0
licznik_cyfr = 0 
licznik_spacji = 0
licznik_znakow_specjalnych = 0

for znak in napis:
    if(znak.isalpha()):
        licznik_liter +=1
    elif(znak.isdigit()):
        licznik_cyfr +=1
    elif(znak.isspace()):
        licznik_znakow_specjalnych +=1
    else:
        licznik_znakow_specjalnych+=1


print(f"Liter jest: {licznik_liter}")
print(f"Liczb jest: {licznik_cyfr}")
print(f"Znakow specjalnych jest: {licznik_znakow_specjalnych}")
