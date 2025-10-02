"""
zahl = int(input("Gib eine Zahl ein, die du durch 3, 10 oder 77 teilen möchtest: "))

if zahl % 3 == 0:
    print("Die Zahl ist durch 3 teilbar.")

if zahl % 3 == 0:
    print("Die Zahl ist durch 10 teilbar.")

if zahl % 3 == 0:
    print("Die Zahl ist durch 77 teilbar.")

else:
    print("Die Zahl ist durch keine der drei Zahlen (3, 10, 77) teilbar.")
"""
"""
zahl = int(input("Gib eine Zahl ein: "))
while zahl > 0:
    print("Hallo")
    zahl -= 1
    pass
"""
"""
#import des Moduls, dass das Ziehen von Werten ermöglicht
import random

#Bereich in dem die Zahl gezogen wird
MINIMUM = 0
MAXIMUM = 100

#Ziehen einer Zufallszahl und Speichern in einer Variable
zufallszahl = random.randint(MINIMUM,MAXIMUM)

#Ausgabe der gezogenen Zahl (nur für Prüfzwecke)
#print(zufallszahl)

antwort = None
versuchszähler = 0



while antwort != zufallszahl:
    
    antwort = int(input("Gib eine Zahl ein: "))

    versuchszähler += 1
    if antwort < zufallszahl:
        print("zu niedrig")
        pass
    elif antwort > zufallszahl:
        print("zu hoch")
        pass
    pass

print ("Herzlichen Glückwunsch, du hast die Zahl erraten!")
print("Zahl: " + str(zufallszahl))
print(f"Versuch: {versuchszähler}")
"""

"""
#
import time

while True:
    antwort = input("Schreib etwas: ")
    if antwort == "exit":
        break

    print("Echo: "+ antwort)
    pass
print("Bis bald.")
#
"""
"""
# er ist 1998 geboren
PIN = "1234"
GEBURTSJAHR = "2012"
PASSWORT = "it"

while True:
    eingabe_pin = input("PIN: ")
    if eingabe_pin != PIN:
        print("Zugang verwigert.")
        continue
 
    eingabe_geburtsjahr = input("GEBURTSJAHR: ")
    if eingabe_geburtsjahr != GEBURTSJAHR:
        print("Zugang verwigert.")
        continue
    
    eingabe_passwort = input("PASSWORT: ")
    if eingabe_passwort != PASSWORT:
        print("Zugang verwigert.")
        continue
    print("Erfolgreich eingeloggt.")
    break
    pass
print("Infos sind hier: ..............")
"""
i = 0
while True:
    if i == 0:
        anfangszahl = int(input("Gib die erste Zahl ein: "))
        zahl = zahl = int(input("Gib die zweite Zahl ein: "))
        zahl = anfangszahl + zahl
        print(f"Die Zahl ist {zahl}")
        pass
    else:
        nächstezahl = int(input("Gib die nächste Zahl ein: "))
        zahl = zahl + nächstezahl
        print(f"Die Zahl ist {zahl}")
        pass
    i=1
    pass
