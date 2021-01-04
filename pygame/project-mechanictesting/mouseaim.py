import pygame, math, random
from pygame.locals import *
WHITE = (255,255,255)
BLACK = (0,0,0)
pygame.init()
size = (640,480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("JUMP")

class player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([40,40])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 320
        self.rect.y = 400
        self.movex = 0
        self.movey = 0
    def move(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val

class bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, speed, targetx, targety):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
##        self.rect.x = x - 5
##        self.rect.y = y - 5
##        self.speed = speed
##        self.targety = targety
##        self.targetx = targetx
        angle = math.atan2(targety-y, targetx-x) #get angle to target in radians
        print("gradient",targety-y, targetx-x)
        print("radian", angle)
        print('Angle in degrees:', int(angle*180/math.pi))
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        print("dx,dy", math.cos(angle), math.sin(angle))
        print("dx,dy speed",self.dx, self.dy)
        self.x = x
        self.y = y
    def update(self):
##        self.rect.y = self.targety
##        self.rect.x = self.targetx
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        self.rect.x = int(self.x) - 5
        self.rect.y = int(self.y) - 5

all_sprites_group = pygame.sprite.Group()
player = player()
all_sprites_group.add(player)
bullet_group = pygame.sprite.Group()

done = False
click = False
clock = pygame.time.Clock()
### -- Game Loop
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-2,0)
    if keys[pygame.K_d]:
        player.move(2,0)
    if keys[pygame.K_w]:
        player.move(0,-2)
    if keys[pygame.K_s]:
        player.move(0,2)

    if event.type == MOUSEBUTTONDOWN:
        if event.button == 1 and click == False:
            click = True
    if click:
        x,y = pygame.mouse.get_pos()
        b = bullet(player.rect.centerx, player.rect.centery, 10, 10, 5, x, y)
        bullet_group.add(b)
        all_sprites_group.add(b)
        click = False
        
    #Next event
    all_sprites_group.update()
    
    screen.fill(BLACK)

    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
