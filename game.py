import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True

while running:
    # This is for handling the shutdown
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # This is for filling the background with color
    screen.fill((30, 30, 30))
    pygame.display.update()

pygame.quit()
