import pygame
import random

map1 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

map2 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

map3 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

map4 = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    ]

my_maps = [map1, map2, map3, map4]
array_enemies = [2, 2, 2, 1]
array_speed = [-1, 1]
array_speed2 = [-3, 3]
my_id = 1
my_score = 0
player_reset = True 

# Set event type
pygame.time.set_timer(pygame.USEREVENT, 2000)
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (1500, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Game")

## CLASSES ##
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(WHITE)
        # Set position
        self.rect = self.image.get_rect()
        self.rect.x = 620
        self.rect.y = 360
        self.lives = 3
        self.move = "UP"

    def player_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val

    def shoot(self):
        bullet = Bullet(self.rect.x + 5, self.rect.y + 5, self.move)
        bullet_group.add(bullet)
        all_sprites_list.add(bullet)

class Wall(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_ref, y_ref):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        
    def update(self):
        pass
    
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos, shoot_pos):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.shoot = shoot_pos
        self.speed = 3

    def update(self):
        if(self.shoot == "LEFT"):
            self.rect.x -= self.speed
        elif(self.shoot == "RIGHT"):
            self.rect.x += self.speed
        elif(self.shoot == "UP"):
            self.rect.y -= self.speed
        elif(self.shoot == "DOWN"):
            self.rect.y += self.speed
    
class NextLevel(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos

    def newPos(self, x_pos, y_pos):
        self.rect.x = x_pos
        print(x_pos)
        self.rect.y = y_pos
        all_sprites_list.add(self)
        next_group.add(self)

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.image = pygame.Surface([20,20])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.speed_x = array_speed[random.randint(0, 1)]
        self.speed_y = array_speed[random.randint(0, 1)]

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.x + 5, self.rect.y + 5, 1)
        enemybullet_group.add(enemy_bullet)
        all_sprites_list.add(enemy_bullet)

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        enemy_hit_wall = pygame.sprite.spritecollide(self, wall_list, False)
        for foo in enemy_hit_wall:
            self.speed_x = array_speed[random.randint(0, 1)]
            self.speed_y = array_speed[random.randint(0, 1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        self.old_x = self.rect.x
        self.old_y = self.rect.y

class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y, speed):
        super().__init__()
        self.image = pygame.Surface([10,10])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.speed = speed
        self.shoot = random.randint(1, 4)

    def update(self):
        if self.shoot == 1:
            self.rect.x -= self.speed
        elif self.shoot == 2:
            self.rect.x += self.speed
        elif self.shoot == 3:
            self.rect.y -= self.speed
        elif self.shoot == 4:
            self.rect.y += self.speed

class Boss(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.image = pygame.Surface([60,60])
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.old_x = self.rect.x
        self.old_y = self.rect.y
        self.speed_x = array_speed2[random.randint(0, 1)]
        self.speed_y = array_speed2[random.randint(0, 1)]
        self.lives = 20

    def shoot(self):
        enemy_bullet = EnemyBullet(self.rect.x + 10, self.rect.y + 10, 5)
        enemybullet_group.add(enemy_bullet)
        all_sprites_list.add(enemy_bullet)

    def delete(self):
        self.kill()

    def update(self):
        self.rect.x = self.rect.x + self.speed_x
        self.rect.y = self.rect.y + self.speed_y
        enemy_hit_wall = pygame.sprite.spritecollide(self, wall_list, False)
        for foo in enemy_hit_wall:
            self.speed_x = array_speed2[random.randint(0, 1)]
            self.speed_y = array_speed2[random.randint(0, 1)]
            self.rect.x = self.old_x
            self.rect.y = self.old_y
        self.old_x = self.rect.x
        self.old_y = self.rect.y

        
        
## END CLASS ## 

## SPRITE GROUP ##
all_sprites_list = pygame.sprite.Group()

player = Player()
all_sprites_list.add(player)

wall_list = pygame.sprite.Group()

bullet_group = pygame.sprite.Group()

next_group = pygame.sprite.Group()

enemy_group = pygame.sprite.Group()

enemybullet_group = pygame.sprite.Group()

## Create Initial Wall ##
def createWall():
    x = 0
    y = 0
    for row in my_maps[my_id]:
        for col in row:
            if col == 1:
                my_wall = Wall(RED, 40, 40, x, y)
                all_sprites_list.add(my_wall)
                wall_list.add(my_wall)
            x = x + 40
        x = 0
        y = y + 40

def createEnemy():
    enemy_num = 0
    for x in range(array_enemies[my_id]):
        enemy = Enemy(random.randrange(200,240),random.randrange(200,240))
        enemy_group.add(enemy)
        all_sprites_list.add(enemy)
        enemy_num += 1
        
createWall()
createEnemy()

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        # -- bullet shot
        elif event.type == pygame.KEYDOWN:
            if event.key == ord('z'):
                player.shoot()

        # User event type
        elif event.type == pygame.USEREVENT:
            # loop through the enemy sprite and call shoot method
            for item in enemy_group:
                item.shoot()
                
    ## Player Movement ## 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.player_speed(-1,0)
        player.move = "LEFT"
        player_reset = False
    elif keys[pygame.K_RIGHT]:
        player.player_speed(1,0)
        player.move = "RIGHT"
        player_reset = False
    elif keys[pygame.K_UP]:
        player.player_speed(0,-1)
        player.move = "UP"
        player_reset = False
    elif keys[pygame.K_DOWN]:
        player.player_speed(0,1)
        player.move = "DOWN"
        player_reset = False

    ## Player Collision with Wall ## 
    player_hit = pygame.sprite.spritecollide(player, wall_list, False)
    for foo in player_hit:
        player.player_speed(0,0)
        player.rect.x = player_old_x
        player.rect.y = player_old_y

    ## Player Collision with Enemy ##
    player_hit_enemy = pygame.sprite.spritecollide(player, enemy_group, False)
    for foo in player_hit_enemy:
        player.rect.x = 620
        player.rect.y = 360
        
        if player_reset == False:
            player.lives -= 1
            player_reset = True
            if player.lives == 0:
                pass
        
    ## Enemy bullet collision with wall ##
    enemybullet_wall = pygame.sprite.groupcollide(enemybullet_group, wall_list, True, False)

    ## Enemy bullet collision with player ##
    enemybullet_player = pygame.sprite.spritecollide(player, enemybullet_group, True)
    for foo in enemybullet_player:
        player.lives -= 1

    ## Enemy collision with wall ##
    enemy_hit_wall = pygame.sprite.groupcollide(enemy_group, wall_list, False, False)
    for foo in enemy_hit_wall:
        pass
        
    ## Bullet Collision with Wall ##
    bullet_wall = pygame.sprite.groupcollide(bullet_group, wall_list, True, False)
        
    ## Enemy Collision with Bullets ##
    if my_id != 3:
        enemy_hit_bullet = pygame.sprite.groupcollide(enemy_group, bullet_group, True, True)
        for foo in enemy_hit_bullet:
            ## Create 'portal' ##
            if(len(enemy_group) == 0):
                my_point = NextLevel(620,360)
                all_sprites_list.add(my_point)
                next_group.add(my_point)
    elif my_id == 3:
            boss_hit = pygame.sprite.groupcollide(enemy_group, bullet_group, False, True)
            for foo in boss_hit:
                boss.lives -= 1
                if boss.lives == 0:
                    boss.delete()

        
            
    ## Collision with 'portal' ##
    player_next = pygame.sprite.spritecollide(player, next_group, True)
    for foo in player_next:
        ## Remove old map ##
        for item in wall_list:
            item.kill()
        ## Point system ##
        if (len(enemy_group) == 0):
            if player.lives == 3:
                my_score = my_score + 10
            elif player.lives == 2:
                my_score = my_score + 5
            elif player.lives == 1:
                my_score = my_score + 2
        ## Create new map ##
        player.lives = 3
        my_id += 1
        createWall()
        if my_id != 3:
            createEnemy()
        if my_id == 3:
            boss = Boss(1100, 240)
            enemy_group.add(boss)
            all_sprites_list.add(boss)
                
    ## Player old pos values ##
    player_old_x = player.rect.x
    player_old_y = player.rect.y    

    all_sprites_list.update()
    screen.fill(BLACK)
    
    font = pygame.font.Font(None, 25)
    livesText = font.render('Lives: ' + str(player.lives), True, WHITE)
    screen.blit(livesText, (1300, 20))

    scoreText = font.render('Score: ' + str(my_score), True, WHITE)
    screen.blit(scoreText, (1300, 40))

    if my_id == 3:
        healthText = font.render('Boss Health: ' + str(boss.lives), True, WHITE)
        screen.blit(healthText, (600, 40))
        if (len(enemy_group)) == 0:
            winText = font.render('You Win', True, WHITE)
            screen.blit(winText, (600, 360))
    ## Powerup ## 
    if my_score > 9:
        for item in bullet_group:
            item.speed = 9
        if my_score > 14:
            for item in bullet_group:
                item.image = pygame.Surface([20,20])
                item.image.fill(GREEN)
    
    # --- Drawing code should go here
    all_sprites_list.draw(screen)
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to x frames per second
    clock.tick(250)
 
# Close the window and quit.
pygame.quit()
