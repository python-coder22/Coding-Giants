"""
#frage nach zahlen und erstelle die summe
#wenn exit == eingabe, beende das programm

summe = 0
while True:
    eingabe = input("Gib eine Zahl ein (oder 'exit' zum Beenden): ")
    if eingabe == "exit":
        print("Programm beendet.")
        print("Deine Summe ist:", summe)
        break
    else:
        summe += int(eingabe)
"""
"""
range(10)  # Gibt eine Sequenz von Zahlen von 0 bis 9 zurück

range(0,10)  # Gibt eine Sequenz von Zahlen von 0 bis 9 zurück
range(0, 10, 1)  # Gibt eine Sequenz von Zahlen von 0 bis 8 in Schritten von 1 zurück

range(2,10)  # Gibt eine Sequenz von Zahlen von 2 bis 9 zurück

range(2,10,1)  # Gibt eine Sequenz von Zahlen von 2 bis 9 in Schritten von 1 zurück


range(2,10,3)  # Gibt eine Sequenz von Zahlen von 2 bis 8 in Schritten von 3 zurück
"""
"""
for elem in range(5,10,2):
    print(elem)
    pass
"""
"""
#0,1,2,3,4

for elem in range(0, 5, 1):
    print(elem)
    pass
"""
"""
alter_jahrgang = 13

for i in range(alter_jahrgang + 1):
    kalender_jahr = 2025 - alter_jahrgang + i
    alter_im_jahr = i
    print(f"Im Jahr {kalender_jahr} warst du {alter_im_jahr} Jahre alt.")
"""
"""
for a in range(5):
    print(f"a= {a}")
    for b in range(20,70,10):
        print(f"\tb = {b}")
        pass
    pass
"""
"""
# Erstelle eine Multiplikationstabelle von 1 bis 100
# Die Tabelle soll 10x10 sein, wobei die Werte zentriert und durch "|" getrennt sind.
for a in range(1,11):
    line = ""
    for b in range(1,11):
        line += str(a*b).center(4) + "|"
        pass
    print(line)
    pass
"""
"""
wert =int(input("Gib eine Zahl ein: "))
for a in range(wert):
    print(f"a = {a}")
    if a > 4:
        break
    pass
else:
    print("Die Schleife wurde ohne die break-Anweisung ausgeführt.")
    pass
"""
"""
# Pyramide aus Sternchen mit maximaler Höhe 5 und maximaler Breite 10
höhe = 5
max_breite = 10
print("Pyrsmide:")
for i in range(1, höhe + 1):
    sterne = 2 * i - 1
    zeile = "*" * sterne
    print(zeile.center(max_breite))
"""
# Ausgefülltes Rechteck mit Sternchen ausgeben
breite = 10
höhe = 5
print("Ausgefülltes Rechteck:")
for i in range(höhe):
    print("*" * breite)