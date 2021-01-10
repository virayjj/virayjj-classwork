import pygame
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
pygame.init()
size = (800,600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Stamina")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 300
    def move(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val
all_sprites_list = pygame.sprite.Group()
player = Player()
all_sprites_list.add(player)
done = False
clock = pygame.time.Clock()
stamina = 150
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        player.move(-1,0)
    if keys[pygame.K_d]:
        player.move(1,0)
    if keys[pygame.K_w]:
        player.move(0,-1)
    if keys[pygame.K_s]:
        player.move(0,1)
    
    if keys[pygame.K_a] and keys[pygame.K_j] and stamina > 1:
        player.move(-4,0)
        stamina = stamina - 2
    if keys[pygame.K_d]and keys[pygame.K_j] and stamina > 1:
        player.move(4,0)
        stamina = stamina - 2
    if keys[pygame.K_w]and keys[pygame.K_j] and stamina > 1:
        player.move(0,-4)
        stamina = stamina - 2
    if keys[pygame.K_s]and keys[pygame.K_j] and stamina > 1:
        player.move(0,4)
        stamina = stamina - 2

    if not keys[pygame.K_j]:
        if stamina != 150:
            stamina = stamina + 1
    
    player.update()
    screen.fill(BLACK)
    font = pygame.font.Font(None, 25)
    txt = font.render("press 'j' to sprint    " + str(stamina), True, WHITE)
    screen.blit(txt, (400, 100))
    all_sprites_list.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
