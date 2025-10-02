anzahl_der_tickets = int(input("Gib die Anzahl der Tickets ein: "))
monatsnummer = int(input("Gib die Monatsnummer ein: "))

if monatsnummer in (1, 2, 12):
    preis = 50
elif monatsnummer in (3, 4, 10, 11):
    preis = 100
elif monatsnummer in (5, 6, 8, 9):
    preis = 200
elif monatsnummer == 7:
    preis = 250
else:
    print("Ungültige Monatsnummer eingegeben. Bitte versuche es erneut.")
    exit()
gesamtpreis = anzahl_der_tickets * preis
print(f"Ticketpreis: {gesamtpreis} EUR")
