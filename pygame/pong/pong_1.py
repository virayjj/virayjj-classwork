import pygame
# -- Global Constants

# -- Colours
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of window
pygame.display.set_caption("Pong")
# -- Exit game flag set to false
done = False
# -- Variables
ball_width = 20
x_val = 150
y_val = 200
x_direction = 1
y_direction = 1
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- GAME LOOP
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next Event
    # -- Game logic goes after this comment
    x_val = x_val + x_direction 
    y_val = y_val + y_direction 
    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,20))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End while - End of game loop
pygame.quit()
