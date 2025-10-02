"""
Schreibe ein Python-Programm, das eine Punktzahl zwischen 0 und 100 vom 
Benutzer abfragt und je nach Punktzahl eine Bewertung ausgibt.
Die Bewertung soll folgendermaßen erfolgen:
Wenn die Punktzahl zwischen 90 und 100 liegt, gib "Sehr gut" aus.
Wenn die Punktzahl zwischen 75 und 89 liegt, gib "Gut" aus.
Wenn die Punktzahl zwischen 60 und 74 liegt, gib "Befriedigend" aus.
Bei allen Punktzahlen unter 60 soll "Nicht bestanden" ausgegeben werden.
"""
note = int(input("Wie viele Punkte hast du bei der Prüfung erreicht? "))

if note < 0 or note > 100:
    print("Fehler bei der Eingabe.!")
else:
    if note >= 90:
        print("Sehr gut.")
    elif note >= 75:
        print("Gut.")
    elif note >= 60:
        print("Befriedigend.")
    else:
        print("Nicht bestanden.")
