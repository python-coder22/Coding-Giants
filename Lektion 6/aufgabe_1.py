"""
Enthält das eingegebene Wort einen Buchstaben / eine Zeichenkette?
Schreibe ein Programm, das überprüft, ob im angegebenen Text der Buchstabe 'a', 'd', die
Zeichenkette "as" oder "zzz" enthalten ist. 
Zeige eine Nachricht an, wenn eine der oben genannten Bedingungen erfüllt ist.
"""

satz = (input("Gib einen beliebigen Satz ein: "))

if "a" in satz or "d" in satz or "as" in satz or "zzz" in satz:
    print("Mindestens eines der gesuchten Schlüsselwörter sind im Satz enthalten.")