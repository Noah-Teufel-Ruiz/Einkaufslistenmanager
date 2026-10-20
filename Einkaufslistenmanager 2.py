
def aktion_hinzufügen():
    global einkaufsliste
    artikel = input("Welchen Artikel möchtest du hinzufügen? ")
    einkaufsliste.append(artikel)
    print(artikel, "wurde zur Einkaufsliste hinzugefügt.")


def aktion_anzeigen():
    global einkaufsliste
    print("Deine Einkaufsliste:")
    for artikel in einkaufsliste:
        print("-", artikel)

def aktion_entfernen():
    global einkaufsliste
    artikel = input("Welchen Artikel möchtest du entfernen? ")
    if artikel in einkaufsliste:
        einkaufsliste.remove(artikel)
        print(artikel, "wurde aus der Einkaufsliste entfernt.")
    
def aktion_beenden():   
    print("Programm beendet!")
    global weitermachen
    weitermachen = False


einkaufsliste = []
weitermachen = True
while weitermachen:
    aktion = input("Möchtest du einen Artikel (h)inzufügen, die Liste (a)nzeigen, einen Artikel (e)ntfernen oder das Programm (b)eenden? ").lower()

    
    
    if aktion == "h":
        aktion_hinzufügen()
    elif aktion == "a":
        aktion_anzeigen()
    elif aktion == "e":
        aktion_entfernen()
    elif aktion == "b":
        aktion_beenden()
    else:
        print("Ungültige Eingabe. Bitte wähle 'h', 'a', 'e' oder 'b'.")