auswahl = 0
saldo = 0

def nutzerauswahl():
    auswahl = int(input("Bitte wählen Sie eine Option (1-4): "))
    return auswahl

def hauptmenue():
    print("Hauptmenü")
    print("1. Geld einzahlen")
    print("2. Geld abheben")
    print("3. Kontostand prüfen")
    print("4. Beenden")

def betrag_abfragen(text):
    return float(input(text))
    
def geld_einzahlen(a_saldo):
    einzahlungs_betrag = betrag_abfragen("Geben Sie den Betrag ein: ")
    a_saldo = a_saldo + einzahlungs_betrag
    kontostand_anzeigen(a_saldo)
    return a_saldo

def geld_abheben(a_saldo):
    auszahlungs_betrag = betrag_abfragen("Geben Sie einen Betrag ein: ")
    if auszahlungs_betrag > a_saldo:
        print("Ihr Geld auf dem Konto ist größer, als das was Sie auszahlen möchten.")
        return a_saldo
    else:
        a_saldo = a_saldo - auszahlungs_betrag
        kontostand_anzeigen(a_saldo)
        return a_saldo
def kontostand_anzeigen(a_saldo):
    print(f"Ihr aktueller Kontostand: {a_saldo}€.")
    
while auswahl != 4:
    hauptmenue()
    auswahl = nutzerauswahl()

    if auswahl == 1:
        saldo = geld_einzahlen(saldo)
    elif auswahl == 2:
        saldo = geld_abheben(saldo)
    elif auswahl == 3:
        kontostand_anzeigen(saldo)
    elif auswahl == 4: pass
        
    else:
        print("Ungültige Eingabe.")
