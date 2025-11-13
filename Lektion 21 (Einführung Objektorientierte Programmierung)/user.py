class User():
    vorname = ""
    nachname = ""
    alter = 0

    def anzeigen(self):
        print(self.vorname, self.nachname)
        if self.alter >= 18:
            print(f"{self.vorname} ist {self.alter} Jahre alt und ist erwachsen:")
        else:
            print(f"{self.vorname} ist {self.alter} Jahre alt und ist nicht erwachsen.")

    def alter_aendern(self, neues_alter):
        self.alter = neues_alter



class Fach():
    durchschnitt = 0

    def liste_erstellen(self):
        self.noten = []

    def note_hinzufügen(self,note):
        self.noten.append(note)
        self.durchschnitt = sum(self.noten) / len(self.noten)

    def noten_anzeigen(self):
        print("Liste der Noten:",self.noten)
    
    def durchschnitt_anzeigen(self):
        print(f"Durchschnitt: {self.durchschnitt}")



class Tisch():
    breite = 200
    hoehe = 60
    laenge = 140

    def anzeigen(self):
        print(f"Breite: {self.breite}cm.")
        print(f"Höhe: {self.hoehe} cm.")
        print(f"Länge: {self.laenge} cm.")
        print()

    def aendere_breite(self, neue_breite):
        self.breite = neue_breite
    
    def aendere_hoehe(self, neue_hoehe):
        self.hoehe = neue_hoehe

    def aendere_laenge(self, neue_laenge):
        self.andere_laenge = neue_laenge
        

#Ha freiwillig ab hier..
class Kontostand():
    gehalt_in_tage = 200
    gehalt_pro_stunde = 25
    vermögen = 100000
    #-----------
    gehalt_in_tage_EM = 600000000
    gehalt_pro_stunde_EM = 25000000
    vermögen_EM = 500000000000

    def anzeigen(self):
        print(f"Das Gehalt am Tag eines durchschnittlichem Deutschen beträgt ca.: {self.gehalt_in_tage}.")
        print(f"Das Gehalt in einer Stunde eines durchschnittlichem Deutschen beträgt ca.: {self.gehalt_pro_stunde}.")
        print(f"Das Vermögen eines durchschnittlichem Deutschen beträgt ca.: {self.vermögen}.")

    def anzeigen_Elon_Musk(self):
        print(f"Das Gehalt am Tag von Elon Musk beträgt ca.: {self.gehalt_in_tage_EM}.")
        print(f"Das Gehalt in einer Stunde von Elon Musk beträgt ca.: {self.gehalt_pro_stunde_EM}.")
        print(f"Das Vermögen von Elon Musk beträgt ca.: {self.vermögen_EM}.") 
