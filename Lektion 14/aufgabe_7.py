import random

def zufallszahlen_liste(n):
    return [random.randint(0, 100) for _ in range(n)]

# Beispielaufrufe
liste1 = zufallszahlen_liste(5)
liste2 = zufallszahlen_liste(5)
liste3 = zufallszahlen_liste(5)

print(liste1)
print(liste2)
print(liste3)