""""
alter = int(input('Gib dein Alter ein'))
"""

''''
a = 10
b = 7
print(b-a)  #minus
print(-a)   #minuswert
print(a-b)  #minus
print(b * a)#mal
print(b/a)  #geteilt
print(b%a)  #modolu
print(a//b) #
print(3 ** 2)   #potenz

a = 3
b = 4

a = a +2
print(a)

a += 2
print(a)

a-= 5
print(a)

b*=a
print(b)

b/=2
print(b)

a %= 2
print(a)
a = 7
a //= 2
print(a)

b **= a
print(b)

print(True + True)
print(False + True)
print(False + False)
print(3*True)

print('Hallo' + 'Freund')

print(3*'test')
print('test' *3)

text = 'Text'
new_text = 'neuer '
new_text += text    #new_text = new_text + text
print(new_text)

n = 10
m = 25
print('Ergebnis der Multiplikation', n, 'mal', m, 'ist', n*m)
print(f'Ergebnis der Addition von {n} und {m} ist {n+m}')

#Mathematisch
print(abs(-10))
print(max(1,2,3,8, -5))
print(min(1,-5,8))
print(round(3.5644))

#Iterierbar
print(len('Hello World!'))

name = input('Gib deinen Namen ein: ')
geburtsdatum = input('Gib deinen Geburtsdatum ein: ')

print('Vorname: ' + name)
print('Geburtsdatum: ' + geburtsdatum)

a = int(input('Gib eine Zahl ein: '))
b = int(input('Gib eine zweite Zahl ein: '))

print('Lösung: ' + f'{a//b}{a%b}')

c = a//b
d = a%b
print('Lösung: ' + f'{c},{d}')

zahl = int(input('Gib eine Zahl ein: '))
prozent = int(input('Gib einen Prozentsatz ein: '))

ergebnis = zahl * prozent / 100
print((f"{prozent}% von {zahl} sind {ergebnis}"))


faktor = 3.6

m_s = float(input("Gib die Geschwindigkeit in Metern pro Sekunde ein: "))
km_h = m_s * faktor
print(f"{m_s} m/s sind {km_h} Meter pro Stunde.")
'''
#von hier...
a = int(input("Gib die Seite a ein: "))
b = int(input("Gib die Seite b ein: "))

import math
hypotenuse = math.sqrt(a * a + b *b)
print(f"Die Hypotenuse des Dreiecks mit den Seiten {a} und {b} beträgt: { hypotenuse}")
#... bis hier von Daniel die Aufgabe