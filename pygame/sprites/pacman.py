import pygame

# -- Global Constants
# -- Array position
map = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,0,1,1,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,1,1,1,0,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
# -- Colours
BLACK = (0,0,0)
BLUE = (50,50,225)
RED = (255,0,0)

# -- Initialise PyGame
pygame.init()
# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)
# -- Title of new window/screen
pygame.display.set_caption("Pac man")


## -- Define the class tile which is a sprite
class tile(pygame.sprite.Sprite):
    def __init__(self, color, width, height, x_ref, y_ref):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = x_ref
        self.rect.y = y_ref
        
class Player(pygame.sprite.Sprite):
    def __init__(self):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([10,10])
        self.image.fill(RED)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 20
        self.rect.y = 20

    def player_update_speed(self, x_val, y_val):
        self.rect.x += x_val
        self.rect.y += y_val


# Create a list of all sprites
all_sprites_list = pygame.sprite.Group()

# Create a list of tiles for the walls
wall_list = pygame.sprite.Group()

# Add player sprite to sprite list
pacman = Player()
all_sprites_list.add(pacman)

# Create walls on the screen (each tile is 20 x 20 so alter cords)
for y in range(10):
    for x in range (10):
        if map[y][x] == 1:
            my_wall = tile(BLUE, 20, 20, x*20, y*20)
            wall_list.add(my_wall)
            all_sprites_list.add(my_wall)

  
# -- Exit game flag set to false
done = False
# -- Manages how fast screen refreshes
clock = pygame.time.Clock()
### -- Game Loop
while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    
    # Pacman hit walls
    pacman_hit = pygame.sprite.spritecollide(pacman, wall_list, False)
    for hit in pacman_hit:
        pacman.player_update_speed(0,0)
        pacman.rect.x = pacman_old_x
        pacman.rect.y = pacman_old_y

    # Reset pos of pacman
    pacman_old_x = pacman.rect.x
    pacman_old_y = pacman.rect.y
        
    # Player key press (continuous)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman.player_update_speed(-1,0)
        #print("LEFT")
    elif keys[pygame.K_RIGHT]:
        pacman.player_update_speed(1,0)
        #print("RIGHT")
    elif keys[pygame.K_UP]:
        pacman.player_update_speed(0,-1)
        #print("UP")
    elif keys[pygame.K_DOWN]:
        pacman.player_update_speed(0,1)
        #print("DOWN")
        
                    
    # -- Update all sprite group
    all_sprites_list.update()    

    # -- Clear screen
    screen.fill(BLACK)

    # -- Draw all sprite group
    all_sprites_list.draw(screen)

    # -- Update the full display Surface to the screen
    pygame.display.flip()
    
    # -- The clock ticks over
    clock.tick(60)
#End While - End of game loop
pygame.quit()
