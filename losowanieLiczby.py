import random #biblioteka do losowania liczb
print("Zgadywanka liczbowa")

wylosowana = int(random.randrange(1,100)) #jak chce sie uzyc metody z biblioteki to .metoda
zgadywana = int(input("Zgaduj liczbe!: ")) 

while(wylosowana != zgadywana):
    if(wylosowana>zgadywana):
        print("Twoja liczba jest za mala")
    elif(wylosowana<zgadywana):
        print("Twoja liczba jest za duza")
    zgadywana = int(input("Sprobuj jeszcze raz: ")) 

print("Udalo sie zgadnac!!")