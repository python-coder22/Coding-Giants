import pygame
import element

FENSTER_BREITE = 800
FENSTER_HOEHE = 600

hintergrund_bild = pygame.image.load('background.png')

charakter_basis_bild = pygame.image.load('base.png')
pygame.init()

anzeige = pygame.display.set_mode([FENSTER_BREITE, FENSTER_HOEHE])
uhr = pygame.time.Clock()

kopf = element.KopfBedeckung()
kleidung = element.Kleidung()
augen = element.Augen()
waffen = element.Waffen()

spiel_aktiv = True
while spiel_aktiv:

    for ereignis in pygame.event.get():
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_ESCAPE:
                spiel_aktiv = False

        elif ereignis.type == pygame.QUIT:
            spiel_aktiv = False

    anzeige.blit(hintergrund_bild,(0,0))

    anzeige.blit(charakter_basis_bild,(270,130))

    anzeige.blit(kleidung.ausgewaehltes_bild(),(270,130))
    anzeige.blit(waffen.ausgewaehltes_bild(),(270,130))
    anzeige.blit(augen.ausgewaehltes_bild(),(270,130))
    anzeige.blit(kopf.ausgewaehltes_bild(),(270,130))
    pygame.display.flip()

    uhr.tick(30)

pygame.quit()