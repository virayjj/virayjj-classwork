import pygame
import random
import math

# -- Global Constants
# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)
RED = (255,0,0)

pause = False
# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Space Invaders")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([10,10])
        self.image.fill(YELLOW)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = size[1] - 10
        self.speed = 0
        self.lives = 5
        self.bullet_count = 50
        self.score = 0

    def player_set_speed(self, val):
        if(self.rect.x < 0):
            self.rect.x = 0
        elif(self.rect.x > size[0] - 10):
            self.rect.x = size[0] - 10
        else:
            self.rect.x += val

    def bullet_shoot(self):
        bullet = Bullet(self.rect.x + 3, self.rect.y - 4)
        bullets_group.add(bullet)
        all_sprites_group.add(bullet)
        self.bullet_count = self.bullet_count - 1

    def update(self):
        if pause == True:
            self.kill()
        

class Invader(pygame.sprite.Sprite):
    def __init__(self):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([10,10])
        self.image.fill(BLUE)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 600)
        self.rect.y = random.randrange(-50, 0)
        self.speed = 1
        
    def update(self):
        self.rect.y = self.rect.y + self.speed
        if self.rect.y == 480:
            self.rect.x = random.randrange(0, 600)
            self.rect.y = random.randrange(-50, 0)
        if pause == True:
            self.kill()
    #End Procedure

     
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([4, 4])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.speed = 5
    
    def update(self):
        self.rect.y = self.rect.y - self.speed
        if pause == True:
            self.kill()
#End Class
      
# -- Exit game flag set to false
done = False

# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()
# 
invaders_group = pygame.sprite.Group()
#
bullets_group = pygame.sprite.Group()

player = Player()
all_sprites_group.add(player)

# Create the invaders
number_of_invaders = 10
for x in range(number_of_invaders):
    invaders = Invader()
    invaders_group.add(invaders)
    all_sprites_group.add(invaders)


# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # -- bullet single shot
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if pause == False: 
                    player.bullet_shoot()
                
                
    # -- Player key press, left and right (continuous)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.player_set_speed(-3)
    if keys[pygame.K_RIGHT]:
        player.player_set_speed(3)
    #Next event


    # update all sprite group
    all_sprites_group.update()

    # bullets hit invaders
    invaders_hit = pygame.sprite.groupcollide(invaders_group, bullets_group, True, True)
    for foo in invaders_hit:
        player.score = player.score + 5
        print(player.score)

    # invader reset
    for hit in invaders_hit:
        invaders = Invader()
        all_sprites_group.add(invaders)
        invaders_group.add(invaders)
    
    # invaders hit player
    player_hit = pygame.sprite.spritecollide(player, invaders_group, True)
    for foo in player_hit:
        player.lives = player.lives - 1
        print(player.lives)
        
    
    screen.fill(BLACK)

    if player.lives == 0 or player.bullet_count == 0:
        pause = True
        
    # -- Display lives, score and bullets
    font = pygame.font.Font(None, 25)	 
    livesText = font.render('Lives: ' + str(player.lives), True, WHITE)
    screen.blit(livesText, (20, 20))

    bulletsText = font.render('Bullets: ' + str(player.bullet_count), True, WHITE)
    screen.blit(bulletsText, (20, 50))

    scoresText = font.render('Score: ' + str(player.score), True, WHITE)
    screen.blit(scoresText, (20, 80))

    all_sprites_group.draw(screen)

    # -- Display score at end
    if pause == True:
        pygame.draw.rect(screen, BLACK, (0, 0, 640, 480))
        finalText = font.render('Final Score Is: ' + str(player.score), True, WHITE)
        screen.blit(finalText, (240, 240))


    # -- flip display to reveal new position of objects
    pygame.display.flip()
    # - The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
