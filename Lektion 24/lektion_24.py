from random import randint, choice

class Charakter:

    def __init__(self,leben, max_leben):
        self.name = ""
        self.leben = leben
        self.max_leben = max_leben
        
    def angriff_durchfuehren(self, gegner):
        schaden = randint(0,3)

        if schaden == 0:
            print(f"{gegner.name} weicht dem Angriff von {self.name} aus.")

        else:
            print(f"{self.name} greift {gegner.name} an und verursacht {schaden} Schaden.")
            gegner.leben -= schaden
        
class Gegner(Charakter):
    def __init__(self,spieler):
        super().__init__()
        self.name = choice(['Goblin', 'Skellet', 'Zombie'])
        self.leben = randint(1,spieler.leben)

class Spieler(Charakter):
    def __init__(self,leben):
        super().__init__((leben))
        self.name = input("Gib den Namen ein.")


    def ausruhen(self):
        if self.leben > self.max_leben:
            self.leben = self.max_leben

        print(f"{self.name} ruht sich aus. Leben: {self.leben}/{self.max_leben}")

    def kaempfen(self,gegner):
        kampf = True
        while kampf:
            print(f"Leben des Spielers: {self.leben}")
            print(f"Leben von {gegner.name}: {gegner.leben}")
            
            aktion = input("Aktion (angreifen, fliehen): ")

            if aktion == "angreifen":
                self.angriff_durchfuehren(gegner)
                if gegner.leben >= 0:
                    print(f"{self.name} besiegt {gegner.name}")
                    return True
                gegner.angriff_durchfuehren(self)
            elif aktion == "fliehen":
                print(f"{self.name} flieht.")
                gegner.angriff_durchfuehren(self)
                kampf = False
            else:
                print("Unbekannte Aktion.")
            if self.leben <= 0:
                print(f"{self.name} ist gestorben.")
                return False
        return True
    
spieler = Spieler(input("Gib den Namen ein. "),10)
spiel = True
while spiel:
    aktion = input("Aktion, erkunden, ausruhen:" )
    if aktion == "erkunden":
        if randint(0,1) == 0:
            print(f"{spieler.name} hat eine Höhle gefunden.")
        else:
            gegner = Gegner(spieler)
            print(f"{spieler.name} ist auf einem {gegner.name} gestoßen.")
            spiel = spieler.kaempfen(gegner)

    elif aktion == "ausruhen":
        spieler.ausruhen

    else:
        print("Ungültige Aktion.")    