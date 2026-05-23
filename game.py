import pygame
import tile
import random

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()

ice_map = pygame.image.load("assets/ice_map.png")
ice_map = pygame.transform.scale(ice_map, (3000, 3000))
car_img = pygame.image.load("assets/car.png")
car_img = pygame.transform.scale(car_img, (75, 75))
pingviin_img = pygame.image.load("assets/pingviin.png")
pingviin_img = pygame.transform.scale(pingviin_img, (50, 50))
enemy_img = pygame.image.load("assets/enemy.png")
enemy_img = pygame.transform.scale(enemy_img, (60, 60))

#Vaenlase info
enemy = []
enemy_x = 1000
enemy_y = 1000
enemy_speed = 2
vision_range = 1000
enemy_size = 500
spawn_enemy_time = 0

#Pingviinide info
pingviinid = []
spawn_time = 0
ouch_timer = -9999999

#Score cound info
font = pygame.font.SysFont(None, 36)
score = 0
last_score_time = 0

#Maailma enda info
world_x = 0
world_y = 0
world_vx = 0
world_vy = 0
x = 100
y = 100
vx = 0
vy = 0

#Auto info
acceleration = 0.8
friction = 0.98
speed = 5
car_x = screen_width // 2
car_y = screen_height // 2

running = True

while running:
    # This is for handling the shutdown
    clock.tick(60)
    current_time = pygame.time.get_ticks()
    keys = pygame.key.get_pressed()
    car_rect = pygame.Rect(car_x, car_y, 50, 50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if keys[pygame.K_w]:
        world_vy -= acceleration
    if keys[pygame.K_s]:
        world_vy += acceleration
    if keys[pygame.K_a]:
        world_vx -= acceleration
    if keys[pygame.K_d]:
        world_vx += acceleration

    for pingviin in pingviinid:
        ping_rect = pygame.Rect(pingviin[0] - world_x, pingviin[1] - world_y, 40, 40)
        if car_rect.colliderect(ping_rect):
            score += 5
            ouch_timer = pygame.time.get_ticks()
            pingviinid.remove(pingviin)

    world_vx *= friction
    world_vy *= friction

    world_x += world_vx
    world_y += world_vy

    if current_time - spawn_time > 5000:
        print("SPAWN WORKING")
        for i in range(400):
            rand_x = random.randint(-30000, 30000)
            rand_y = random.randint(-30000, 30000)
            pingviinid.append([rand_x, rand_y])
        spawn_time = current_time

    if current_time - spawn_enemy_time > 5000:
        print("SPAWN ALSO WORKING")
        for i in range(100):
            rand_x = random.randint(-30000, 30000)
            rand_y = random.randint(-30000, 30000)
            enemy.append([rand_x, rand_y])
        spawn_enemy_time = current_time

    # This is for filling the background with color
    screen.fill((30, 144, 255))
    tile.draw_tiles(screen, world_x, world_y, screen_width, screen_height)

    for pingviin in pingviinid:
        screen.blit(pingviin_img, (pingviin[0] - world_x, pingviin[1] - world_y))

    player_world_x = car_x + world_x
    player_world_y = car_y + world_y

    for e in enemy:
        dx = player_world_x - e[0]
        dy = player_world_y - e[1]
        distance = (dx * dx + dy * dy) ** 0.5
        if distance < vision_range and distance != 0:
            e[0] += enemy_speed * (dx / distance)
            e[1] += enemy_speed * (dy / distance)
        enemy_rect = pygame.Rect(e[0] - world_x, e[1] - world_y, 40, 40)
        screen.blit(enemy_img, (e[0] - world_x, e[1] - world_y))

        if car_rect.colliderect(enemy_rect):
            print("GAME OVER")
            running = False

    screen.blit(car_img, (car_x, car_y))

    if pygame.time.get_ticks() - ouch_timer < 1000:
        font_big = pygame.font.SysFont(None, 72)
        ouch_text = font_big.render("OUCH", True, (255, 0, 0))
        screen.blit(ouch_text, (screen_width // 2 - 80, screen_height // 2))

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
