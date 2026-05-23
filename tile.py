import pygame

tile_size = 256

ice_tile = pygame.image.load("assets/ice_map.png")
ice_tile = pygame.transform.scale(ice_tile, (tile_size, tile_size))

def draw_tiles(screen, world_x, world_y, screen_width, screen_height):
    start_x = int(world_x) // tile_size * tile_size
    start_y = int(world_y) // tile_size * tile_size

    for x in range(start_x - screen_width, start_x + screen_width * 2, tile_size):
        for y in range(start_y - screen_height, start_y + screen_height * 2, tile_size):
            screen.blit(ice_tile, (x - world_x, y - world_y))
