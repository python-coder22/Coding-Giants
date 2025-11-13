import math
class Tier():
    def __init__(self,alter,name):
        self.alter = alter
        self.name = name

    def geraeusch_machen(self):
        print(f"{self.name} macht ein Geräusch.")

    def fressen(self):
        print(f"{self.name} frisst.")

tier1 = Tier(8, "Felix")
tier1.geraeusch_machen()
tier1.fressen()

print()
print(" ")
print(" ")

class Hund(Tier):

    def __init__(self,alter,name):
        super().__init__(alter, name)
        self.rasse = "Mops"

    def rasse_anzeigen(self):
        print(f"{self.name} ist ein {self.rasse}.")
hund1 = Hund(8, "Rex")
hund1.geraeusch_machen()
hund1.fressen()
hund1.rasse_anzeigen()

print(" ")

class Katze(Tier):

    def __init__(self,alter,name):
        super().__init__(alter, name)
        self.rasse = "Siam-Katze"

    def rasse_anzeigen(self):
        print(f"{self.name} ist ein*e {self.rasse}.")
katze1 = Katze(8, "Lucy")
katze1.geraeusch_machen()
katze1.fressen()
katze1.rasse_anzeigen()

#vogel von tier (f. fliegen)
#adler von vogel (f. jagen)

class Vogel(Tier):

    def __init__(self,alter,name):
        super().__init__(alter, name)
        self.rasse = "Amsel"

    def rasse_anzeigen(self):
        print(f"{self.name} ist ein*e {self.rasse}.")

    def fliegen(self):
        print(f"{self.name} kann fliegen.")
vogel1 = Vogel(8, "Paul")
vogel1.geraeusch_machen()
vogel1.fressen()
vogel1.rasse_anzeigen()
vogel1.fliegen()

class Adler(Vogel):

    def __init__(self,alter,name):
        super().__init__(alter, name)
        self.rasse = "Stein Adler"

    def rasse_anzeigen(self):
        print(f"{self.name} ist ein*e {self.rasse}.")

    def jagen(self):
        print(f"{self.name} kann jagen.")
adler1 = Adler(8, "Elias")
adler1.geraeusch_machen()
adler1.fressen()
adler1.rasse_anzeigen()
adler1.jagen()



class Kreis():
    radius = 0
    def __init__(self,r):
        self.radius = r * 0

class Rechteck():
    def __init__(self,b,h):
        self.b = b
        self.h = h




PI = 3.1415

class Figur:
    def flaeche_anzeigen(self):
        print(f"Fläche: {self.flaeche}")

    def umfang_anzeigen(self):
        print(f"Umfang: {self.umfang}")

    def flaeche_anzeigen(self, name):
        print(self.flaeche)



class Kreis(Figur):
    def __init__(self, r):
        super().__init__("Kreis")
        self.r = r
        self.flaeche = PI * r



class Rechteck(Figur):
    def __init__(self, x, y):
        super().__init__("Rechteck")
        self.x = x
        self.y = y
        self.flaeche = x * y
        self.umfang = x + y + x + y

figuren = [Kreis(5), Rechteck[3,5]]

for figur in figuren:
    print(figur.flaeche)