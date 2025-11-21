import pygame
import element

FENSTER_BREITE = 800
FENSTER_HOEHE = 600

hintergrund_bild = pygame.image.load('background.png')

charakter_basis_bild = pygame.image.load('base.png')
pygame.init()

meine_schrift = pygame.font.SysFont('Comic Sans MS', 30)

anzeige = pygame.display.set_mode([FENSTER_BREITE, FENSTER_HOEHE])
uhr = pygame.time.Clock()

kopf = element.KopfBedeckung()
kleidung = element.Kleidung()
augen = element.Augen()
waffen = element.Waffen()

def zeige_text(anzeige, text, position):
    nachicht = meine_schrift.render(text, False, (255,255,255))
    anzeige.blit(nachicht,position)

spiel_aktiv = True
speichern = False
laden = False

y_c = 130
counter = 1

while spiel_aktiv:


    for ereignis in pygame.event.get():
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_ESCAPE:
                spiel_aktiv = False

            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_q:
                    kopf.waehle_naechstes()
            
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_e:
                    kleidung.waehle_naechstes()
            
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_w:
                    augen.waehle_naechstes()
            
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_r:
                    waffen.waehle_naechstes()
            
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_s:
                    speichern = True
            
            if ereignis.type == pygame.KEYDOWN:
                if ereignis.key == pygame.K_t:
                    laden = True
        elif ereignis.type == pygame.QUIT:
            spiel_aktiv = False

    anzeige.blit(hintergrund_bild,(0,0))

    anzeige.blit(charakter_basis_bild,(270,y_c))

    if y_c == 130 or y_c == 110:
        counter *= -1
    y_c += counter
    
    anzeige.blit(charakter_basis_bild,(270,y_c))
    anzeige.blit(kleidung.ausgewaehltes_bild(),(270,y_c))
    anzeige.blit(waffen.ausgewaehltes_bild(),(270,y_c))
    anzeige.blit(augen.ausgewaehltes_bild(),(270,y_c))
    anzeige.blit(kopf.ausgewaehltes_bild(),(270,y_c))

    if speichern:
        pygame.image.save(anzeige,'character.png')
        speichern = False
    
    if laden:
        pygame.image.load(anzeige,'character.png')
        laden = False
    
    zeige_text(anzeige,f'[Q] Kopf: {kopf.gewaehlt}' ,(100,100))
    zeige_text(anzeige,f'[W] Augen: {augen.gewaehlt}' ,(100,140))
    zeige_text(anzeige,f'[E] Kleidung: {kleidung.gewaehlt}' ,(100,180))
    zeige_text(anzeige,f'[R] Waffe: {waffen.gewaehlt}' ,(100,220))
    zeige_text(anzeige,f'[S] Speichern: Speichern ', (100,360))
    zeige_text(anzeige, f'[T] Laden: Laden', (100,380))

    pygame.display.flip()

    uhr.tick(30)

pygame.quit()