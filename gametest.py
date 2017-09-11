
import os, pygame
from pygame.locals import *
from pygame.compat import geterror

try:
    import sys
    import random
    import math
    import os
    import getopt
    import pygame
    from socket import *
    from pygame.locals import *
except ImportError, err:
    print "couldn't load module. %s" % (err)
    sys.exit(2)

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

# Recheck this; deals with tile-based things
# Got this from qq after searching how to deal with tiles
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

class Unit(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_png('bunny.png')
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.topleft = 100, 100
        self.move = 20
    def update(self):
        self.move = 20


def main():
    """this function is called when the program starts.
       it initializes everything it needs, then runs in
       a loop until the function returns."""
#Initialize Everything
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Test junk')
    pygame.mouse.set_visible(0)

#Create The Backgound
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

#Put Text On The Background, Centered
    if pygame.font:
        font = pygame.font.Font(None, 36)
        text = font.render("Text Test 1", 1, (10, 10, 10))
        textpos = text.get_rect(centerx=background.get_width()/2)
        background.blit(text, textpos)

#Display The Background
    screen.blit(background, (0, 0))
    pygame.display.flip()

# Prepare Game Objects
    clock = pygame.time.Clock()

    unit = Unit()
    allsprites = pygame.sprite.RenderPlain(unit)

# Tileset
    table = load_tile_table("tileset1.png", 24, 16)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*32, y*24))
    pygame.display.flip()

    going = True
    while going:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        #Draw Everything
        allsprites.update()

        #Draw Everything
        screen.blit(background, (0, 0))
        allsprites.draw(screen)
        pygame.display.flip()

    pygame.quit()



if __name__=='__main__':
    pygame.init()
    screen = pygame.display.set_mode((128, 98))
    screen.fill((255, 255, 255))
    table = load_tile_table("ground.png", 24, 16)
    for x, row in enumerate(table):
        for y, tile in enumerate(row):
            screen.blit(tile, (x*32, y*24))
    pygame.display.flip()
    while pygame.event.wait().type != pygame.locals.QUIT:
        pass
