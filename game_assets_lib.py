### game_assets_lib
import pygame
import os
pygame.mixer.init()
from start import WIDTH, HEIGHT



### RAW IMAGES
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_yellow.png'))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join('Assets', 'spaceship_red.png'))
SPACE = pygame.image.load(os.path.join('Assets', 'space.png'))

### BULLETS
YELLOW_BULLETS = [] # [(bullet_rect, bullet_img)]
MAX_YELLOW_BULLETS = 10

### HEALTH
YELLOW_HEALTH = 1
RED_HEALTH = 2


'''
    Scaled and rotated images
'''
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 65, 65
BULLET_WIDTH, BULLET_HEIGHT = 20, 20

YELLOW_SPACESHIP_START_X, YELLOW_SPACESHIP_START_Y = WIDTH/2 - (WIDTH/4) - SPACESHIP_WIDTH/2, HEIGHT/2
RED_SPACESHIP_START_X, RED_SPACESHIP_START_Y = WIDTH/2 + (WIDTH/4) - SPACESHIP_WIDTH/2, HEIGHT/2

YELLOW_SPACESHIP_UP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_UP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))

YELLOW_SPACESHIP_RIGHT = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_RIGHT = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)

YELLOW_SPACESHIP_DOWN = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)
RED_SPACESHIP_DOWN = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 180)

YELLOW_SPACESHIP_LEFT = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)
RED_SPACESHIP_LEFT = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

    #since I do not have an image of a bullet, I will just scale down the yellow space ship so that it looks like
    #a bullet :)

YELLOW_BULLET_UP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT))
YELLOW_BULLET_RIGHT = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)), 90)
YELLOW_BULLET_DOWN = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)), 180)
YELLOW_BULLET_LEFT = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (BULLET_WIDTH, BULLET_HEIGHT)), 270)

SPACE_TRANSFORMED = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))


### SOUNDS

HIT_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Grenade+1.mp3'))

BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('Assets', 'Gun+Silencer.mp3'))
BULLET_FIRE_SOUND.set_volume(0.25)