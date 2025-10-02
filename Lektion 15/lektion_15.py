def dezimal_zu_binaer(dezimal: int) -> str:
    if dezimal == 0:
        return "0"
    
    ergebnis = ""
    while dezimal > 0:
        rest = dezimal % 2       
        ergebnis = str(rest) + ergebnis
        dezimal //= 2
    return ergebnis


zahl = int(input("Gib eine Dezimalzahl ein: "))
print("Die Binärzahl lautet:", dezimal_zu_binaer(zahl))
