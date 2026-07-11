

beenden = True
einkaufsliste = []


while beenden:

    funktion = input("Was willst du machen? \n " \
    "1. Artikel hinzufügen, drücke h \n" \
    "2. Einkaufsliste anzeigen, drücke a \n" \
    "3. Artikel entfernen, drücke e \n" \
    "4. Beenden, drücke b \n  ").lower()

    if funktion.lower() == "h":
        artikel_hinzufügen = input("Welchen Artikel willst du hinzufüen? ")
        einkaufsliste.append(artikel_hinzufügen)
        print(f"Artikel {artikel_hinzufügen} wurde hinzugefügt.")

    elif funktion.lower() == "a":
        print("-", einkaufsliste)

    elif funktion.lower() == "e":
        artikel_entfernen = input("Welchen Artikel willst du entfernen? ")

        if artikel_entfernen in einkaufsliste:
            einkaufsliste.remove(artikel_entfernen)
            print(f"Artikel {artikel_entfernen} wurde entfernt.")


    elif funktion.lower() == "b":
        beenden = False
        print("Programm wird beendet.")

    else:
        print("Ungültige Eingabe.")
