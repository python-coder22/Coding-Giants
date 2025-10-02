Mathe = float(input("Geb deine Mathe Note ein : "))
Deutsch = float(input("Geb deine Deutsch Note ein : "))
Englisch = float(input("Geb deine Englisch Note ein: "))
Geschichte = float(input("Geb deine Geschichte Note ein: "))
Sport = float(input("Geb Sport Note ein: "))

summe = Mathe+Deutsch+Englisch+Geschichte+Sport
durchschnitt = summe /5 

print("Dein Notendurchschnitt ist: ", durchschnitt) 

if durchschnitt <= 1.5:
    print("Du erhältst das Zeugnis mit Auszeichnung.")
else:
    print("Du erhältst kein Zeugnis mit Auszeichnug")
    