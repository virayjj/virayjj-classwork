import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (225,255,0)

pygame.init()

size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Window")

done = False
sun_x = 40
sun_y = 100

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    sun_x = sun_x + 5

    screen.fill (BLACK)
    
    pygame.draw.rect(screen, BLUE, (220,165,200,150))
    pygame.draw.circle(screen, YELLOW, (sun_x,sun_y),40,0)
                     
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
