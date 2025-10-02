"""
def begruessung(name):
    print(f"Hallo, {name}")

begruessung("Thomas")
nickname = "Tom"
begruessung(nickname)
"""
"""
def begruessung(name, wiederholung):
    for i in range(wiederholung):
        print(f"Hallo, {name}!")
    pass

begruessung("Thomas", 1)
nickname = "Tom"
begruessung(nickname, 5)
"""
"""
def rechteck_flaeche(breite, hoehe):
    flaeche = breite * hoehe
    print(f"Fläche: {flaeche}")
    pass
rechteck_flaeche(10, 29)
"""
"""
import time
def ladebalken(fertig,alles=100):
    #Das Zeichen "#" bedeutet einen erledigten Teil
    #Das Zeichen "-" bedeutet einen nicht erledigten Teil

    #Umrechnung des Fortschritts von "alles" auf 10
    erledigt = round((10 * fertig) / alles)
    unerledigt = 10 - erledigt

    text_erledigt = '#' * erledigt
    text_unerledigt = '-' * unerledigt
    #[##--------]
    print(f'\r[{text_erledigt}{text_unerledigt}]',end=' ')
for i in range(100):
    ladebalken(i, 100)
    #ladebalken
    time.sleep(0.258)
"""
"""
#n ist die anzahl an wiederholungen
#a ist die startzahl einer schleife
#hää?

def foo(a, n):
    for i in range(a, a+n):
        print(f"{i}^2 = {i ** 2}")
foo(5,4 )
"""
"""
import math
from math import sqrt

def flaeche_sechseck(a):
    return 3* sqrt(3) * a**2 / 2

def volumen_prisma(seitenlaenge, hoehe):
    return flaeche_sechseck(seitenlaenge) * hoehe
print(f"Das Volumen des Prismas beträgt: {volumen_prisma(35, 5)}")
print(f"Die Fläche des Sechsecks beträgt: {flaeche_sechseck(35)}")
"""

def Array_sum(erstes,zweites,drittes):
    array = []
    array.append(erstes)
    array.append(zweites)
    array.append(drittes)
    Summe = erstes + zweites + drittes
    array.append(Summe)
    return array

print(Array_sum(3,7,2))