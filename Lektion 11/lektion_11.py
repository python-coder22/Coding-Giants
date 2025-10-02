"""
#aufgabe 1
def foo(phrase, arr_words):

    return phrase.join(arr_words)
    

print(foo("?",["felix","ist","nett"]))

#aufgabe2 

def teilbar(zahl, divisor):
    if divisor == 0:
        return "Man kann nicht durch 0 teilen"
    elif zahl % divisor == 0:
        return f"Die Zahl {zahl} ist durch {divisor} teilbar"
    else:
        return f"Die Zahl {zahl} ist nicht durch {divisor} teilbar"
    
print(teilbar(2,3))
print(teilbar(7,0))
print(teilbar(4,2))
"""
"""
#aufgabe3

def rechteck(a: int, b: int) -> float:
    umfang = 2 * a + 2 * b
    return umfang
print(rechteck(4, 4))
"""
"""
#aufgabe4
def nachicht(name: str, alter: int, größe:float) -> str:
    return f"{name} ist {alter} Jahre alt, {größe:.2f} m groß."

print(nachicht("Markus",22,1.89657568))
print(nachicht("Lena",23,1.5))

"""
"""
#aufgabe5
def anmelden(Richtiger_Login: str,Richtiges_Passwort: str) -> bool:
    benutzername = input("Benutzername: ")
    passwort = input("Passwort: ")
    if benutzername == Richtiger_Login and passwort == Richtiges_Passwort:
        return True
    else:
        return False
"""
"""

    #Kürzere Variante
    return benutzername == Richtiges_Passwort and passwort == Richtiger_Login

def anmelden_mit_versuchen(versuche: int, Richtiger_Login: str,Richtiges_Passwort: str) -> bool:
    versuche = max(1,versuche)

    for versuch in range(versuche):
        if anmelden(Richtiger_Login, Richtiges_Passwort):
            return True
        else:
            print(f"Fehlerhafter Versuch Nr. {versuch+1}")
            pass

        print("Login fehlgeschlagen.")
    return False

print(anmelden_mit_versuchen(3, "Ananas", "Baum"))

"""
# Aufgabe 6
import random
def Random_array(Size,Randmin,Randmax):
    Liste = []
    for elem in range(Size):
        zufallszahl = random.randint(Randmin, Randmax)
        Liste.append(zufallszahl)
    return Liste

print(Random_array(5, 10, 30)) 
