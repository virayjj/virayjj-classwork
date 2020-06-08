### SRC - Really good code works well

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
x_direction = -1
y_direction = 1
padd_length = 15
padd_width = 60
x_padd = 0
y_padd = 20
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- GAME LOOP
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    keys = pygame.key.get_pressed()
    ## - the up key or down key has been pressed
    if keys[pygame.K_UP]:
        y_padd = y_padd - 5
    if keys[pygame.K_DOWN]:
        y_padd = y_padd + 5
       
    if y_padd < 0:
        y_padd = 0
    if y_padd > 420:
        y_padd = 420
            #End If
        #End If
    #Next Event
    
    
    # -- Game logic goes after this comment
    x_val = x_val + x_direction 
    y_val = y_val + y_direction 
    
    if x_val < padd_length and y_val > y_padd and y_val < y_padd + padd_width:
        x_direction = x_direction * -1
        
    if y_val == 460 or y_val == 0:
        y_direction = y_direction * -1
        
    if x_val == 620:
        x_direction = x_direction * -1
        
    if x_val == -20:
        x_val = 200
        y_val = 200
        pygame.draw.rect(screen, BLUE, (x_val, y_val, 20, ball_width))
        
    # -- Screen background is BLACK
    screen.fill (BLACK)
    # -- Draw here
    pygame.draw.rect(screen, BLUE, (x_val,y_val,ball_width,20))
    pygame.draw.rect(screen, WHITE, (x_padd, y_padd, padd_length, padd_width))
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End while - End of game loop
pygame.quit()
