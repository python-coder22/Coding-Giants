
"""

bedingungen =  True
if bedingung:
    print("Die Bedingung ist wahr")


print("ananas")#
"""
"""
dividend = int(input("Gib den Dividend ein: "))
divisor = int(input("Gib den Divisor ein: "))

if divisor != 0:
    ergebnis = dividend / divisor
    print("Das Ergebnis der Devision:", ergebnis)

if divisor == 0:#
    print("Man kann nicht durch Null teilen!")

"""
"""
bedingungen =  True
if bedingung:
    #Code falls wahr ist
    pass
else:
    #unser Code falls False
    #falls alle anderen
"""
"""
#Freizeitparkattraktion
alter = int(input("Gib dein Alter ein: "))
größe =  int(input("Gib deine Körpergröße ein: "))

if alter >= 12 and 130 <= größe <= 195:
    print("Ja, du darfst die Attraktion nutzen.")

else:
    print("Nein, du darfst die Attraktion nicht nutzen.")
"""
"""
if bedingung:
    #falls wahr
    pass
elif bedingung2:
    #falls vorherige bedingungen nicht erfüllt wurde und bedingung 2 wahr ist
    pass
else:
    #falls alle vorherigen bedingungen nicht erfüllt wurden
    pass
"""
"""
zahl = int(input("Gib eine Zahl ein: "))

if zahl > 0:
    print("positive Zahl")
elif zahl < 0:
    print("Negative Zahl")
elif zahl == 0:
    print("Null wurde eingegeben")
"""
"""
#Urlaubspreis ausrechner
monat_nummer = int(input("Gib die Monatsnummer ein: "))

if 1<= monat_nummer <= 2:
    print("Der Preis beträgt $150.")
elif 3 <= monat_nummer <= 4 or 11 <= 12:
    print("Der Preis beträgt $199.")
elif 5 <= monat_nummer <= 6 or monat_nummer == 10:
    print("Der Preis beträgt $249.")
elif 7 <= monat_nummer <= 9:
    print("Der Preis beträgt $299.")
else:
    print("Bitte gib eine gültige Monatnummer ein.")
"""
"""  
#Taschenrechner
print("+ Addition, - Subtraktion, * Multiplikation, / Division")
operator = input("Wähle einen der Oben genannten Operatoren aus: ")

a = float(input("Gib die erste Zahl ein: "))
b= float(input("Gib die zweite Zahl ein: "))

if operator == '+':
    ergebnis = a + b
elif operator == '-':
    ergebnis = a - b
elif operator == '*':
    ergebnis = a * b
elif operator == '/':
    if b == 0:
        print("Man kann nicht durch Null teilen")
        ergebnis = "Fehler"
    else:
        ergebnis = a / b
else:
    print("ungültiges Symbol eingegeben")
    ergebnis = "Fehler"

print(a, operator, b, "=", ergebnis)
"""