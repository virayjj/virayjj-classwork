### SRC - Excellent effort, I really like the detail with the sky.
import pygame

# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
ORANGE = (255,165,0)
GREEN = (0,255,0)
RED = (255,0,0)
LIGHT_BLUE = (173,216,230)
BROWN = (165,42,42)
NAVY = 	(0,0,128)
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (590,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("House")
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
# -- Decalring variables for the position of the sun
sun_x = 0
### SRC - Why aren't you using the coefficients below? You are doing a few
### unnecessary calculations here.
sun_y = int(((sun_x**2) / 2048) - ((5 * sun_x) / 16) + 100)

# coefficient's for quadratic equation of sun movement
a = 0.000976563
b = -0.625
c = 150
### -- Game Loop

while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #End If
    #Next event
    # -- Game logic goes after this comment
    sun_x = sun_x + 5

    if sun_x == 640:
        sun_x = 0

    if sun_x in range(0,160):
        screen.fill(NAVY)
    if sun_x in range(160,320):
        screen.fill(LIGHT_BLUE)
    if sun_x in range(320,480):
        screen.fill(LIGHT_BLUE)
    if sun_x in range(480,640):
        screen.fill(NAVY)

    #Next event
    sun_x = sun_x + 1
    if sun_x > 640:
        sun_x = -40
    sun_y = int(a * sun_x**2 + b * sun_x + c)
    # -- Draw here
    pygame.draw.circle(screen, YELLOW, (sun_x, sun_y),40,0)
    pygame.draw.rect(screen, GREEN, (0,240,640,240))
    pygame.draw.rect(screen, BLUE, (220,330,200,150))
    pygame.draw.rect(screen, BLACK, (220,330,200,150), 3)
    pygame.draw.rect(screen, LIGHT_BLUE, (240,350,35,35))
    pygame.draw.rect(screen, BLACK, (240,350,35,35), 3)
    pygame.draw.rect(screen, LIGHT_BLUE, (365,350,35,35))
    pygame.draw.rect(screen, BLACK, (365,350,35,35), 3)
    pygame.draw.rect(screen, LIGHT_BLUE, (240,425,35,35))
    pygame.draw.rect(screen, BLACK, (240,425,35,35), 3)
    pygame.draw.rect(screen, LIGHT_BLUE, (365,425,35,35))
    pygame.draw.rect(screen, BLACK, (365,425,35,35), 3)
    pygame.draw.rect(screen, BROWN, (295,400,50,80))
    pygame.draw.rect(screen, BLACK, (295,400,50,80), 3)
    pygame.draw.polygon(screen, RED,((190,330), (320,235), (450,330)))
    pygame.draw.polygon(screen, BLACK,((190,330), (320,235), (450,330)), 3)
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()


