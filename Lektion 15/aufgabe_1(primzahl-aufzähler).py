def primzahl(zahl):
    if zahl < 2:
        return False
    for i in range (2, zahl):
        if zahl % i == 0:
            return False
    return True

#Kann man auch weglassen (
def generiere_primzahlen(a, b):
    for i in range(a, b + 1):
        if primzahl(i):
            print(i)

generiere_primzahlen(0, 1000)
#                         )

