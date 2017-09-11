#!/usr/bin/python

import pygame, sys, os
from pygame.locals import *

def load_png(name):
    # Load image and return image object
    # Got from the pygames tutorial
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error, message:
        print 'Cannot load image:', fullname
        raise SystemExit, message
    return image, image.get_rect()

def load_tile_table(filename, width, height):
    fullname = os.path.join('data', filename)
    image = pygame.image.load(fullname).convert()
    image_width, image_height = image.get_size()
    tile_table = []
    for tile_x in range(0, image_width/width):
        line = []
        tile_table.append(line)
        for tile_y in range(0, image_height/height):
            rect = (tile_x*width, tile_y*height, width, height)
            line.append(image.subsurface(rect))
    return tile_table

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((600, 800))
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((150, 150, 150))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Test", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)
    screen.blit(background, (0, 0))

# Tiles
    screen = pygame.display.set_mode((600, 800))
    table = load_tile_table("tileset1.png", 24, 16)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))

        for x, row in enumerate(table):
            for y, tile in enumerate(row):
                screen.blit(tile, (x*32, y*24))
        pygame.display.flip()


if __name__=='__main__':
    pygame.init()
    main()
