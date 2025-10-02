"""
Schreibe ein Python-Programm, das den Benutzer nach zwei Informationen fragt:
Der aktuellen Temperatur (als Zahl in Grad Celsius)
Ob es regnet (mit einer Eingabe wie "ja" oder "nein")
Anhand dieser Eingaben soll das Programm eine Kleidungsempfehlung geben.
"""
"""
-Wenn es kalt ist (unter 10 Grad) und es regnet, soll die Ausgabe sein:
"Es ist kalt und nass – zieh eine Regenjacke und einen Schal an!"
-Wenn es kalt ist, aber nicht regnet, soll die Ausgabe sein:
"Es ist kalt – zieh dich warm an!"
-Wenn es warm ist (10 Grad oder mehr) und es regnet, soll die Ausgabe sein:
"Es regnet – nimm einen Regenschirm mit!"
-Wenn es warm ist und nicht regnet, soll die Ausgabe sein:
"Das Wetter ist angenehm – du brauchst keine besondere Kleidung."
"""

temperatur = int(input("Gib die aktuelle Gradzahl? "))
antwort = input("Regnet es gerade? ")

if temperatur < 10:
    if antwort == "ja" or antwort == "JA" or antwort == "Ja" or antwort == "jA":
        print("Es ist kalt und nass; zieh eine Regenjacke und einen Schal an!")
    else:
        print("Es ist kalt; zieh dich warm an!")
else:
    if antwort == "ja":
        print("Es regnet; nimm einen Regenschirm mit!")
    else:
        print("Das Wetter ist angenehm; du brauchst keine besondere Kleidung.")

