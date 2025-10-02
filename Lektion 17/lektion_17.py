null = ["0", "null"]
eins = ["1", "eins", "einser"]
plus = ["+", "plus", "addiere", "hinzufügen"]

basis = [null, eins, plus]

text = input("Gib den Text ein: ")
rechnung = ""

def uebersetzen(a_wort):
    for symbol_basis in basis:
        for wort_symbol in symbol_basis:
            if a_wort == wort_symbol:
                return symbol_basis[0]
    return''


for wort in text.split(" "):
    rechnung += uebersetzen(wort)
print(rechnung)

def berechne(zahl1, zahl2, a_operation):
    if a_operation == '+':
        return zahl1 + zahl2
    elif a_operation == '-':
        return zahl1 - zahl2
    elif a_operation == '*':
        return zahl1 * zahl2
    elif a_operation == '/':
        return zahl1 / zahl2
def berechne_aus_text(a_text):
    ergebnis = 0 
    zahl = ''
    operation = ''
    for zeichen in text:
        if zeichen.isdigit():
            zahl += zeichen
        elif zahl:
            if operation == '':
                ergebnis = int(zahl)
            else:
                ergebnis = berechne(ergebnis, int(zahl), operation) 
            zahl = ''
            operation = zeichen
    if zahl:
        ergebnis = berechne(ergebnis, int(zahl), operation)
    return ergebnis
print(berechne_aus_text(rechnung)) 
