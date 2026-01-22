# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("My First Pygame Program")
clock = pygame.time.Clock()
running = True
dt = 0
# want to import an image TBD
image_surface = pygame.image.load("python/assets/playerShip1_red.png").convert_alpha()
image_surface = pygame.transform.scale(image_surface, (100, 75))

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)
    screen.blit(image_surface, image_surface.get_rect(center=player_pos))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
    
    # player_pos.x = max(40, min(screen.get_width() - 40, player_pos.x))
    if player_pos.x > screen.get_width()+40:
        player_pos.x = -40
    if player_pos.x < -40:
        player_pos.x = screen.get_width() + 40
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()