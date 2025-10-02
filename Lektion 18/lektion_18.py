import random

wuerfel = [2,1,3,6,4]

def wuerfeln(waehl_wuerfel :str):
    for i in waehl_wuerfel:
        wuerfel[int(i)-1] = random.randint(1,6)

wuerfeln("12345")
print(wuerfel)

def zeige_wuerfel():
    print("__________________")
    print("")
    for i in range(len(wuerfel)):
        print(f"{i+1}.{wuerfel[i]}")
    print("__________________")

zeige_wuerfel()

def frage_neuwurf():
    antwort = input("Möchtest Du neu würfeln? (j/n)  ")
    print("")
    if antwort.lower() == "j":
        return True
    else:
        return False
    
punktname = ["Einsen","Zweien","Dreien","Vieren","Fünften","Sechsen"]
punkte = ["","","","","",""]

def zeige_punktetabelle():
    print("__________________")
    for i in range(len(punkte)):
        print(f"{i+1}. {punktname[i]}\t{punkte[i]}")
    print("__________________")   

def eintrag_zahlenwert(zahl):
    punktzahl = 0
    for w in wuerfel:
        if w == zahl:
            punktzahl += w
    punkte[zahl-1] = punktzahl

def eintrag_punkte():
    feld = int(input("In welches Feld möchtest du die Punkte eintragen (Nummer eingeben): "))
    if 1 <= feld <= 6:
        eintrag_zahlenwert(feld)
    else:
        print("Wähle zwischen 1-13!")
        eintrag_punkte()


for runde in range(len(punkte)):
    wuerfeln("12345")
    zeige_punktetabelle()
    zeige_wuerfel()
    for i in range(2):
        erneut = frage_neuwurf()
        if erneut:
            auswahl = input("Gib die Nummern der Würfel an, die du Würfeln möchtest (ohne Leerzeichen)  ")
            wuerfeln(auswahl)
            zeige_wuerfel()
        else:
            break
    
    zeige_punktetabelle()
    zeige_wuerfel() 
    eintrag_punkte()
    zeige_punktetabelle

print(f"Dein Endergebnis ist:{sum(punkte)}")
