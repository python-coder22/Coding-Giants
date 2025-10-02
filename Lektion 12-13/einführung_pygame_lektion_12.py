import pygame  #import des moduls

pygame.init()  #initialisierung des moduls

#erstellung eines Fensters mit besimmter abmessung
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


screen_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

#Variable die angibt ob das fenster geschlossen werden soll
game_status = True

#Festlegen des Fenstertitels
pygame.display.set_caption("Erstes Spiel")

#Erstellung einer Uhr die eine konstante FPS-Rate überwacht
clock=pygame.time.Clock()


def load_image(img_path: str, position):
    image = pygame.image.load(img_path)  #Laden des Bildes
    surface = image.convert()
    
    transparent_color = (0,0,0)
    surface.set_colorkey(transparent_color)  #Setze die transparente Farbe

    #Die Position wird im rect gespeichert
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def print_image(img_list)-> None:
    image, surface, rect = img_list
    screen_surface.blit(surface, rect)
    pass



player_position = [SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2]  # FIX: Liste statt Tuple
player = load_image("player.png", player_position)  #Laden des Spielers

def set_position_image(img_list, position):
    image, surface, rect = img_list
    rect = surface.get_rect(center=position)
    return [image, surface, rect]

def calculate_player_movement(keys):

    speed = 10
    delta_x = 0
    delta_y = 0

    if keys[pygame.K_LSHIFT]:
        speed *= 2

    if keys[pygame.K_w]:
        delta_y -= speed
    if keys[pygame.K_s]:
        delta_y += speed
    if keys[pygame.K_d]:
        delta_x += speed
    if keys[pygame.K_a]:
        delta_x -= speed
    
    return delta_x, delta_y   # FIX: Rückgabe ergänzt


#Code wird ausgeführt solange das Fenster offen ist
while game_status:
    #Auslesen der vom system regestrierten Ereignisse
    events = pygame.event.get()
    for event in events:  #Kommentiere diese Zeile aus um zu sehen, welche Ereignisse registriert werden
        #wenn du die maus bewegst oder eine Taste drückst
        print(event)  #Ausgabe der Ereignisse in der Konsole

        #Überprüfe ob das Fenster geschlossen wurde  # FIX: nach innen verschoben
        if event.type == pygame.QUIT:
            game_status = False
    pass

    pressed_key = pygame.key.get_pressed()  #Abfrage der gedrückten Tasten
    

    delta_x, delta_y = calculate_player_movement(pressed_key)
    player_position[0] += delta_x
    player_position[1] += delta_y

    player = set_position_image(player, player_position)

    screen_surface.fill((0, 0, 0))  # Bildschirm vor jedem Frame löschen
    print_image(player)  #Zeichnen des Spielers auf dem Bildschirm
    pygame.display.update()  #Aktualisierung des Fensters
    clock.tick(60)  #Begrenzung der FPS auf 60
    pass
pygame.quit()  #Beenden des Moduls
# Überprüfen, ob das Skript direkt ausgeführt wird
# (optional, aber gute Praxis)
if __name__ == "__main__":
    pygame.quit()
    quit()

