import pygame

pygame.init()

clock = pygame.time.Clock()
fps = 60
blue = pygame.Color(33, 175, 74)
black = pygame.Color(0, 0, 0)
screen_width = 400
screen_height = 400
white = pygame.Color(255, 255, 255)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Shadow Mazers')
tile_size = 20  # map size of tile
time = 0
# OOP CLASSES FOR PLAYER AND MAP
class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        for num in range(1, 5):
            img_right = pygame.image.load(f'img/guy{num}.png')
            img_right = pygame.transform.scale(img_right, (20, 20)) 
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.direction = 0
        self.light = pygame.image.load("circle.png")
        self.light = pygame.transform.scale(self.light, (200, 200)) 

    def update(self):
        dx = 0
        dy = 0
        walk_cooldown = 5

        # get keypresses
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            dx -= 5

            self.counter += 1
            self.direction = -1
        if key[pygame.K_UP]:
            dy -= 5

        if key[pygame.K_DOWN]:
            dy += 5

        if key[pygame.K_RIGHT]:
            dx += 5

            self.counter += 1
            self.direction = 1

        if self.counter > walk_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
            if self.direction == -1:
                self.image = self.images_left[self.index]
        for tile in world.tile_list:
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                dy = 0

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.bottom > screen_height:
            self.rect.bottom = screen_height
            dy = 0
        
        screen.blit(self.image, self.rect)
        if self.rect.y==320 and self.rect.x==340:
              print("congrats you won")
              pygame.quit()
# this part was copied from stackoverflow due to my inexperience an dnot being able to make this
        light_rect = self.light.get_rect(center=self.rect.center)
        filter = pygame.surface.Surface((screen_width, screen_height))
        filter.fill((255, 255,255))
        filter.blit(self.light, light_rect)
        screen.blit(filter, (0, 0), special_flags=pygame.BLEND_RGBA_SUB)
        # till here


class World():
    def __init__(self, data):
        self.tile_list = []
        brick_img = pygame.image.load('img/path.png')
        path_img = pygame.image.load('path.png')
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 2:
                    img = pygame.transform.scale(path_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    blob = Enemy(col_count * tile_size + tile_size // 2, row_count * tile_size + tile_size // 2)
                    blob_group.add(blob)

                col_count += 1
            row_count += 1

    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            pygame.draw.rect(screen, (0, 0, 0), tile[1], 2)



world_data = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,2,2,1,2,2,2,2,2,2,2,1,2,2,2,2,1,2],
    [2,1,2,1,2,1,2,1,1,1,1,1,2,1,2,1,1,1,1,2],
    [2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,1,2,2,1,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,1,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,2,1,2,1,2,1,1,1,2,1,2,1,2,1,2,2],
    [2,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,2,1,1,2,1,2,1,2,1,2,1,2,2,2,1,2,1,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,2],
    [2,1,2,1,1,1,2,1,1,1,2,1,1,1,2,1,3,1,2,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2] ]
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('img/blob.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.move_direction = 1
        self.move_counter = 0

    def update(self):
        self.rect.x += 0
        self.move_counter = 0


blob_group = pygame.sprite.Group()
start=False
bg=pygame.image.load("bg.png")
player = Player(40, 40)
world = World(world_data)
scary=pygame.mixer.Sound("img/scary.wav")
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    screen.blit(bg,(0,0))
    scary.play()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                start=True
    if start:
        world.draw()
        player.update()
        blob_group.update()
        blob_group.draw(screen)

    pygame.display.update()

pygame.quit()