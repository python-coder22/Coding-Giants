import pygame

BILDSCHIRM_BREITE = 1264
BILDSCHIRM_HOEHE = 890

pygame.init()

bildschirm = pygame.display.set_mode([BILDSCHIRM_BREITE, BILDSCHIRM_HOEHE])

uhr = pygame.time.Clock()
hintergrund_bild = pygame.image.load("world_map.jpg")

markierungen = []

groesse = 10

farben_index = 0
farben = [(50, 168, 82),(255,0,0),(0,0,0),(0,255,0),(0,0,255)]


programm_aktiv = True
while programm_aktiv:
    for ereignis in pygame.event.get():
        if ereignis.type == pygame.KEYDOWN:
            if ereignis.key == pygame.K_ESCAPE:
                programm_aktiv = False
            if ereignis.key == pygame.K_s:
                pygame.image.save(bildschrim, "karte.jpg")
            if ereignis.key == pygame.K_DOWN and groesse > 1:
                groesse -= 1
            if ereignis.key == pygame.K_UP and groesse < 25:
                groesse += 1
            if ereignis.key == pygame.K_c:
                farben_index += 1
                if farben_index == len(farben):
                    farben_index = 0
        elif ereignis.type == pygame.QUIT:
            programm_aktiv = False
        elif ereignis.type == pygame.MOUSEBUTTONUP:
            markierungen.append([pygame.mouse.get_pos(),groesse, farben[farben_index]])
    
    
    bildschirm.blit(hintergrund_bild, (0,0))

    pygame.draw.circle(bildschirm, farben[farben_index],pygame.mouse.get_pos(),groesse)

    for  markierung in markierungen:
        pygame.draw.circle(bildschirm, markierung[2],markierung[0], markierung[1])

    pygame.display.flip()
    uhr.tick(60)
pygame.quit()

