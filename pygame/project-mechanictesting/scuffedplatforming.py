import pygame

map1 = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

my_maps = [map1]
my_id = 0

WHITE = (255,255,255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
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
        self.rect.y = 300
        self.movey = 0
    def move(self, x_val):
        self.rect.x += x_val
    def gravity(self):
        self.movey += 1
    def update(self):
        self.rect.y = self.rect.y + self.movey

class block(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_ref, y_ref):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref

all_sprites_group = pygame.sprite.Group()
player = player()
all_sprites_group.add(player)
wall_list = pygame.sprite.Group()

def createWall():
    x = 0
    y = 0
    for row in my_maps[my_id]:
        for col in row:
            if col == 1:
                my_wall = block(YELLOW, 40, 40, x, y)
                all_sprites_group.add(my_wall)
                wall_list.add(my_wall)
            x = x + 40
        x = 0
        y = y + 40

createWall()
      
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
         player.move(-6)
    if keys[pygame.K_d]:
         player.move(6)
         
    if jump is False and keys[pygame.K_w] and hit:
        jump = True
    if jump is True:
        player.rect.y -= vel_y*4
        vel_y -= 1
        if vel_y < -10:
            jump = False
            vel_y = 10

    ## COLLISION ##
    hit = pygame.sprite.spritecollide(player, wall_list, False)
    for foo in hit:
        player.movey = 3
        player.rect.y = player_old_y
        #player.rect.x = player_old_x
        
    player_old_y = player.rect.y
    player_old_x = player.rect.x

    #Next event
    all_sprites_group.update()
    player.gravity()
    
    screen.fill(BLACK)

    all_sprites_group.draw(screen)

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
