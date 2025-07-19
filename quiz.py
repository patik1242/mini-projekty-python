import random
print("Quiz wiedzy")

quiz = {
    "Jaki jest stolica Polski?": "Warszawa",
    "Ile to 5 + 3?": "8",
    "Jaki język programowania tu ćwiczymy?": "Python",
    "Kolor nieba w słoneczny dzień?": "Niebieski",
    "Liczba dni w tygodniu?": "7"
}


pytania = {}

wynik = 0
while(True):
    lista_pytan = list(quiz.keys())
    while len(lista_pytan) > 0:
        pytanie = random.choice(lista_pytan)
        print(f"Pytanie: {pytanie} ")

        odp = input("Podaj odpowiedz: ")

        if(odp.strip().lower() == quiz.get(pytanie).strip().lower()):
            print("Poprawna odpowiedz!")
            wynik+=5
        else:
            print("Niepoprawna odpowiedz")

        plik = open("quiz.txt", "a", encoding="utf-8")
        plik.write(f"Pytanie: {pytanie} - {odp}, wynik = {wynik}\n")
        plik.close()
        lista_pytan.remove(pytanie)

    if(len(lista_pytan) == 0 ):
        print(f"Uzyskales: {wynik}/{len(quiz)*5} ")

        plik = open("quiz.txt", "a", encoding="utf-8")
        plik.write(f"Uzyskales: {wynik}\n\n")
        plik.close()
        
        graj_ponownie = input("Chcesz zagrac jeszcze raz: (t/n): ").lower()
        if(graj_ponownie == "t"):
            wynik = 0 
            continue
        else:
            break
    


    