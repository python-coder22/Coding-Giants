import pygame

class Bild(pygame.sprite.Sprite):
    def __init__(self,pfad):
        super().__init__()
        self.image = pygame.image.load(pfad)

class Element:
    def __init__(self,typ):
        #gewälter Kleidungsindijator
        self.gewaelt = 0 
        #Bildliste
        self.bild_liste = []
        for i in range(1,4):
            pfad = f'{typ}{i}.png'
            geladenes_bild = Bild(pfad)
            self.bild_liste.append(geladenes_bild)

    def waehle_naechstes(self):
        self.gewaelt += 1
        if self.gewaelt > 2:
            self.gewaelt = 0

    def ausgewaehltes_bild(self):
        return self.bild_liste[self.gewaelt].image
    
class KopfBedeckung(Element):
    def __init__(self):
        super().__init__('head')
    
class Augen(Element):
    def __init__(self):
        super().__init__('eye')
    
class Kleidung(Element):
    def __init__(self):
        super().__init__('body')

class Waffen(Element):
    def __init__(self):
        super().__init__('weapon')
