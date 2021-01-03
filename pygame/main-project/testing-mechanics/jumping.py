import pygame
WHITE = (255,255,255)
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

all_sprites_group = pygame.sprite.Group()
player = player()
all_sprites_group.add(player)
      
done = False
jump = False
vel_x = 10
vel_y = 10
clock = pygame.time.Clock()
### -- Game Loop
while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
         player.move(-6,0)
    if keys[pygame.K_d]:
         player.move(6,0)
         
    if jump is False and keys[pygame.K_w]:
        jump = True
    if jump is True:
        player.rect.y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

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
