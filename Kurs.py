print("System zarządzania uczestnikami kursu")

kurs = {}

def dodaj():
    nazwa_kursu = input("Podaj nazwe kursu: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko uczestnika: ").strip().title()
    if nazwa_kursu not in kurs:
        kurs[nazwa_kursu] = {}
    if imie_i_nazwisko in kurs[nazwa_kursu]:
        print("Juz uczestniczy w kursie")
    else:
        kurs[nazwa_kursu][imie_i_nazwisko] = [] 
        print(f"Uczestnik {imie_i_nazwisko} dodany do kursu {nazwa_kursu}")

def ocena():
    nazwa_kursu = input("Podaj nazwe kursu: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko uczestnika: ").strip().title()
    if nazwa_kursu in kurs and imie_i_nazwisko in kurs[nazwa_kursu]:
        ocena = int(input("Podaj ocene (1-6): "))
        if(ocena>=1 and ocena<=6):
            kurs[nazwa_kursu][imie_i_nazwisko].append(ocena)
        print(f"Ocena {ocena} dodana dla uczestnika {imie_i_nazwisko} w {nazwa_kursu}")
    else:
        print("Nie ma takiego uczestnika")

def wyswietl():
    nazwa_kursu = input("Podaj nazwe kursu: ").strip().title()
    if nazwa_kursu in kurs:
        print(f"Uczestnicy kursu {nazwa_kursu}")
        for imie_i_nazwisko in kurs[nazwa_kursu]:
            print(f"- {imie_i_nazwisko}\n")

def srednia():
    nazwa_kursu = input("Podaj nazwe kursu: ").strip().title()
    imie_i_nazwisko = input("Podaj imie i nazwisko uczestnika: ").strip().title()
    if nazwa_kursu in kurs and imie_i_nazwisko in kurs[nazwa_kursu]:
        oceny = kurs[nazwa_kursu][imie_i_nazwisko]
        srednia = sum(oceny)/len(oceny)
        print(f"Srednia ocen uczestnika {imie_i_nazwisko} w kursie {nazwa_kursu}: {round(srednia,2)}") 
    else:
        print("Nie ma takiego uczestnika")

def zapis_do_pliku():
    with open("Kurs.txt", "w", encoding="utf-8") as plik:
        for kurs_nazwa, uczestnicy in kurs.items():
            plik.write(f"Kurs: {kurs_nazwa}\n")
            for osoba, oceny in uczestnicy.items():
                plik.write(f"  - {osoba}: {oceny}\n")
    print("Dane zapisane do pliku Kurs.txt")

def zakoncz():
    print("Zakonczono")
    exit()

menu = {1: dodaj, 2: ocena, 3: wyswietl, 4: srednia, 5:zapis_do_pliku, 6:zakoncz}
print("==MENU==\n 1. Dodaj uczestnika\n 2. Dodaj ocene\n 3.Wyswietl uczestnikow\n"
      "4. Oblicz srednia\n 5.Zapisz do pliku\n 6. Zakoncz")
while(True):
    wybor = int(input("Wybierz numer: "))
    funkcja = menu.get(wybor)
    if(funkcja):
        funkcja()
    else:
        print("Nie ma takiej opcji")