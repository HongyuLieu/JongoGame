## gameDraw
import pygame
pygame.font.init()
from start import WIDTH, HEIGHT

### COLORS
WHITE = (255,255,255)
RED = (255,0,0)
YELLOW = (255,255,0)
######
WINNER_FONT = pygame.font.SysFont('comicsans', 120)
COUNT_DOWN_FONT = pygame.font.SysFont('comicsans', 100)




def draw_window(win: 'current window', background, list_IMG_cor:'a list of tuples : (IMG, cordinates)' = []):

    win.blit(background, (0, 0))

    if len(list_IMG_cor) != 0:
        displayUpdated = _blit_objects(win, list_IMG_cor)

    if not displayUpdated:
        pygame.display.update()


def _blit_objects(win:'current window', list_OBJ_cor:'a list of tuples : (OBJ, cordinates)'):

    displayUpdated = False

    if len(list_OBJ_cor) != 0:
        for tuple in list_OBJ_cor:
            win.blit(tuple[0], tuple[1])

        pygame.display.update()
        displayUpdated = True
    
    return displayUpdated

def appendBulletsToToDraw(toDraw:list, bullets:list):
    for bullet in bullets:
        toDraw.append((bullet[1], (bullet[0].x, bullet[0].y)))


def draw_winner(win: 'current window',background, text):
    text_to_display = WINNER_FONT.render(text, 1 , WHITE)
    win.blit(text_to_display, (WIDTH/2 - text_to_display.get_width()/2, HEIGHT/2 - text_to_display.get_height()/2))
    pygame.display.update()

    for i in range(5):
        count_down_to_display = COUNT_DOWN_FONT.render(str(5 - i), 1 , YELLOW)
        win.blit(background, (0, 0))
        win.blit(text_to_display, (WIDTH/2 - text_to_display.get_width()/2, HEIGHT/2 - text_to_display.get_height()/2))
        win.blit(count_down_to_display, (WIDTH/2 - text_to_display.get_width()/2, HEIGHT/2 - text_to_display.get_height()/2 + 100))
        pygame.display.update()
        pygame.time.delay(1000)
    