zeichnungen_galgen = ["",'''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
 
import random

woerter_liste = ["programmierer", "schleife", "bedingung", "programmiersprache", "schule", "kurs"]

zufallsindex_wort = random.randrange(0, len(woerter_liste))

zufallswort = woerter_liste[zufallsindex_wort]

anzahl_nicht_buchstaben = 0
anzeige_wort = []
for buchstabe in zufallswort:
    if buchstabe.isalpha():   # Überprüfung ob das Zeichen ein Buchstabe ist
        anzeige_wort.append('_')
    else:
        anzeige_wort.append(buchstabe)
        anzahl_nicht_buchstaben += 1

#Wort erraten
anzahl_fehler = 0
anzahl_aufgedeckter_buchstaben = 0
benutzte_buchstaben = []

while anzahl_aufgedeckter_buchstaben < len(zufallswort) - anzahl_nicht_buchstaben:
    print(''.join(anzeige_wort))
    print(zeichnungen_galgen[anzahl_fehler])
    print(f'Benutzer Buchstaben: {",".join(benutzte_buchstaben)}')
    eingegebene_buchstabe = input('Gib einen Buchstaben ein: ')
    
    if eingegebene_buchstabe in benutzte_buchstaben:
        print("Der Buchstabe ist bereits im Wort enthalten.")
        next
    
    benutzte_buchstaben.append(eingegebene_buchstabe)

    if eingegebene_buchstabe in zufallswort:
      for i in range(len(zufallswort)):
          if eingegebene_buchstabe == zufallswort[i]:
              anzeige_wort[i] = eingegebene_buchstabe
              anzahl_aufgedeckter_buchstaben += 1

    else:
        anzahl_fehler += 1
        if anzahl_fehler == 7:
            print(zeichnungen_galgen[anzahl_fehler])
            break
"""
if anzahl_fehler < 7:
    print(f'Glückwunsch!, du hast gewonnen! Das Wort war: {zufallswort}')
else:
    print(f'Leider hast du verloren. Das gesuchte Wort war: {zufallswort}')
"""

if anzahl_aufgedeckter_buchstaben == len(zufallswort):
    print(f'Du hast gewonnen! Das gesuchte wort war: {zufallswort}')
else:
    print(f"Du hast verloren! Das gesuchte wort war: {zufallswort}")
