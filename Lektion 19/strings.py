satz = "DaS iSt eIn KoMuScHeR sAtZ"
print(satz)

neuer_satz = []

for ch in satz:
    if ch.isupper():    #Überprüft ob aktueller Charakter groß ist
        ch.lower()      #Falls ja, wandelt es sich auf klein
    if ch.islower():    #Überprüft ob aktueller Charakter groß ist
        ch.upper()      #Falls ja, wandelt es sich auf groß
    neuer_satz.append(ch)
print(neuer_satz)