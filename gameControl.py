### gameControl
import pygame
import game_assets_lib
from start import WIDTH, HEIGHT

VELOCITY_YELLOW = 6
VELOCITY_RED = 9
VELOCITY_YELLOW_BULLET = 15
VELOCITY_RED_DASH = 10

### HIT EVENTS
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

### YELLOW

def handle_yellow_movement(keys_pressed: list, yellow, yellow_direction):
    
    if keys_pressed[pygame.K_a] and yellow.x - VELOCITY_YELLOW > 0: # YELLOW MOVE LEFT
        yellow_direction, yellow.x = yellow_move_left(yellow.x)

    if keys_pressed[pygame.K_d] and yellow.x + VELOCITY_YELLOW < (WIDTH - game_assets_lib.SPACESHIP_WIDTH) : # YELLOW MOVE RIGHT
        yellow_direction, yellow.x = yellow_move_right(yellow.x)

    if keys_pressed[pygame.K_w] and yellow.y - VELOCITY_YELLOW > 0: # YELLOW MOVE UP
        yellow_direction, yellow.y = yellow_move_up(yellow.y)

    if keys_pressed[pygame.K_s] and yellow.y + VELOCITY_YELLOW < (HEIGHT - game_assets_lib.SPACESHIP_HEIGHT): # YELLOW MOVE DOWN
        yellow_direction, yellow.y = yellow_move_down(yellow.y)

    return yellow_direction
    

def yellow_move_left(yellow_x: 'x_cor_of_yellow before moving'):
    '''
        returns updated_yellow, yellow_new_x

        updated_yellow: The new yellow space ship that had its direction changed after the press
        yellow_new_x
    '''

    updated_yellow = game_assets_lib.YELLOW_SPACESHIP_LEFT # change yellow's direction facing
    yellow_new_x = yellow_x - VELOCITY_YELLOW # move 

    return updated_yellow, yellow_new_x


def yellow_move_right(yellow_x: 'x_cor_of_yellow before moving'):
    '''
        returns updated_yellow, yellow_new_x

        updated_yellow: The new yellow space ship that had its direction changed after the press
        yellow_new_x
    '''

    updated_yellow = game_assets_lib.YELLOW_SPACESHIP_RIGHT # change yellow's direction facing
    yellow_new_x = yellow_x + VELOCITY_YELLOW # move 

    return updated_yellow, yellow_new_x


def yellow_move_up(yellow_y: 'y_cor_of_yellow before moving'):
    '''
        returns updated_yellow, yellow_new_y

        updated_yellow: The new yellow space ship that had its direction changed after the press
        yellow_new_y
    '''

    updated_yellow = game_assets_lib.YELLOW_SPACESHIP_UP # change yellow's direction facing
    yellow_new_y = yellow_y - VELOCITY_YELLOW # move 

    return updated_yellow, yellow_new_y


def yellow_move_down(yellow_y: 'y_cor_of_yellow before moving'):
    '''
        returns updated_yellow, yellow_new_y

        updated_yellow: The new yellow space ship that had its direction changed after the press
        yellow_new_y
    '''

    updated_yellow = game_assets_lib.YELLOW_SPACESHIP_DOWN # change yellow's direction facing
    yellow_new_y = yellow_y + VELOCITY_YELLOW # move 

    return updated_yellow, yellow_new_y

###
### RED 

def handle_red_movement(keys_pressed: list, red, red_direction):
    
    if keys_pressed[pygame.K_LEFT] and red.x - VELOCITY_RED > 0 : # RED MOVE LEFT
        red_direction, red.x = red_move_left(red.x)

    if keys_pressed[pygame.K_RIGHT] and red.x + VELOCITY_RED < (WIDTH - game_assets_lib.SPACESHIP_WIDTH): # RED MOVE RIGHT
        red_direction, red.x = red_move_right(red.x)

    if keys_pressed[pygame.K_UP] and red.y - VELOCITY_RED > 0: # RED MOVE UP
        red_direction, red.y = red_move_up(red.y)

    if keys_pressed[pygame.K_DOWN] and red.y + VELOCITY_RED < (HEIGHT - game_assets_lib.SPACESHIP_HEIGHT): # RED MOVE DOWN
        red_direction, red.y = red_move_down(red.y)

    return red_direction
    

def red_move_left(red_x: 'x_cor_of_red before moving'):
    '''
        returns updated_red, red_new_x

        updated_red: The new red space ship that had its direction changed after the press
        red_new_x
    '''

    updated_red = game_assets_lib.RED_SPACESHIP_LEFT # change yellow's direction facing
    red_new_x = red_x - VELOCITY_RED # move 

    return updated_red, red_new_x


def red_move_right(red_x: 'x_cor_of_red before moving'):
    '''
        returns updated_red, red_new_x

        updated_red: The new red space ship that had its direction changed after the press
        red_new_x
    '''

    updated_red = game_assets_lib.RED_SPACESHIP_RIGHT # change yellow's direction facing
    red_new_x = red_x + VELOCITY_RED # move 

    return updated_red, red_new_x


def red_move_up(red_y: 'y_cor_of_red before moving'):
    '''
        returns updated_red, red_new_y

        updated_red: The new red space ship that had its direction changed after the press
        red_new_y
    '''

    updated_red = game_assets_lib.RED_SPACESHIP_UP # change yellow's direction facing
    red_new_y = red_y - VELOCITY_RED # move 

    return updated_red, red_new_y


def red_move_down(red_y: 'y_cor_of_red before moving'):
    '''
        returns updated_red, red_new_y

        updated_red: The new red space ship that had its direction changed after the press
        red_new_y
    '''

    updated_red = game_assets_lib.RED_SPACESHIP_DOWN # change yellow's direction facing
    red_new_y = red_y + VELOCITY_RED # move 

    return updated_red, red_new_y


### BULLET 

def yellow_bullet_fire(yellow, yellow_direction):
    '''
        returns a bullet to the main bullet list. The bullet is produced based on the direction yellow is facing.
    '''
    if yellow_direction == game_assets_lib.YELLOW_SPACESHIP_RIGHT:
        bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 5 ,5)
        bullet_direction = game_assets_lib.YELLOW_BULLET_RIGHT

    elif yellow_direction == game_assets_lib.YELLOW_SPACESHIP_DOWN:
        bullet = pygame.Rect(yellow.x + yellow.width//2 -2, yellow.y + yellow.height, 5 ,5)
        bullet_direction = game_assets_lib.YELLOW_BULLET_DOWN

    elif yellow_direction == game_assets_lib.YELLOW_SPACESHIP_LEFT:
        bullet = pygame.Rect(yellow.x, yellow.y + yellow.height//2 - 2, 5 ,5)
        bullet_direction = game_assets_lib.YELLOW_BULLET_LEFT

    elif yellow_direction == game_assets_lib.YELLOW_SPACESHIP_UP:
        bullet = pygame.Rect(yellow.x + yellow.width//2 -2, yellow.y, 5 ,5)
        bullet_direction = game_assets_lib.YELLOW_BULLET_UP

    else: # TO DO: if facing other directions
        pass

    return (bullet, bullet_direction)

def red_dash():
    pass

def handle_bullets(yellow_bullets: list, red):
    for bullet in yellow_bullets:
        ## bullet move to be implemented here
        if bullet[1] == game_assets_lib.YELLOW_BULLET_RIGHT:
            bullet[0].x += VELOCITY_YELLOW_BULLET
        
        elif bullet[1] == game_assets_lib.YELLOW_BULLET_DOWN:
            bullet[0].y += VELOCITY_YELLOW_BULLET
        
        elif bullet[1] == game_assets_lib.YELLOW_BULLET_LEFT:
            bullet[0].x -= VELOCITY_YELLOW_BULLET
        
        elif bullet[1] == game_assets_lib.YELLOW_BULLET_UP:
            bullet[0].y -= VELOCITY_YELLOW_BULLET
        
        isRemoved = False
        ## bullet collision to be implemented here
        if red.colliderect(bullet[0]):
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
            isRemoved = True

        ## handle bullet going out of border
        if not isRemoved:
            ##check if out of border
            if (bullet[0].x + bullet[0].width//2 > WIDTH) or (bullet[0].y + bullet[0].height//2 > HEIGHT) or(bullet[0].x + bullet[0].width//2 < 0) or (bullet[0].y + bullet[0].height//2 < 0):
                yellow_bullets.remove(bullet)
                isRemoved = True



def handle_red_charge(yellow, red):
    if yellow.colliderect(red):
        pygame.event.post(pygame.event.Event(YELLOW_HIT))