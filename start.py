WIDTH, HEIGHT = 1200, 800

import pygame
import game_assets_lib
import gameDraw
import gameControl


WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 80

pygame.display.set_caption("jongo Game")

def main():

    yellow = pygame.Rect(game_assets_lib.YELLOW_SPACESHIP_START_X, game_assets_lib.YELLOW_SPACESHIP_START_Y,
     game_assets_lib.SPACESHIP_WIDTH, game_assets_lib. SPACESHIP_HEIGHT)
    red = pygame.Rect(game_assets_lib.RED_SPACESHIP_START_X, game_assets_lib.RED_SPACESHIP_START_Y,
     game_assets_lib.SPACESHIP_WIDTH, game_assets_lib. SPACESHIP_HEIGHT)

    yellow_health = game_assets_lib.YELLOW_HEALTH
    red_health = game_assets_lib.RED_HEALTH
    
    yellow_direction = game_assets_lib.YELLOW_SPACESHIP_RIGHT
    red_direction = game_assets_lib.RED_SPACESHIP_LEFT

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    main() # restart the game

                if event.key == pygame.K_SPACE and len(game_assets_lib.YELLOW_BULLETS) < game_assets_lib.MAX_YELLOW_BULLETS:
                    ##handle bullets of yellow
                    game_assets_lib.YELLOW_BULLETS.append(gameControl.yellow_bullet_fire(yellow, yellow_direction))
                    game_assets_lib.BULLET_FIRE_SOUND.play()

            if event.type == gameControl.YELLOW_HIT:
                game_assets_lib.HIT_SOUND.play()
                yellow_health -= 1

            if event.type == gameControl.RED_HIT:
                game_assets_lib.HIT_SOUND.play()
                red_health -= 1

            winning_message = ""

            ##check if yellow dies
            if yellow_health <= 0:
                winning_message = "GAME OVER! Red Wins!!"

            ##check if red dies
            if red_health <= 0:
                winning_message = "GAME OVER! Yellow Wins!!"

            ##check if someone wins; if yes, stop
            if len(winning_message) != 0:
                game_assets_lib.YELLOW_BULLETS.clear()
                print(winning_message)
                gameDraw.draw_winner(WIN, game_assets_lib.SPACE_TRANSFORMED, winning_message)
                pygame.event.clear()
                main()
                

        keys_pressed = pygame.key.get_pressed()
        yellow_direction = gameControl.handle_yellow_movement(keys_pressed, yellow, yellow_direction)
        red_direction = gameControl.handle_red_movement(keys_pressed, red, red_direction)
        gameControl.handle_bullets(game_assets_lib.YELLOW_BULLETS, red)
        gameControl.handle_red_charge(yellow, red)

        toDraw = [(yellow_direction, (yellow.x, yellow.y)),
                    (red_direction, (red.x, red.y))]
        gameDraw.appendBulletsToToDraw(toDraw, game_assets_lib.YELLOW_BULLETS)


        gameDraw.draw_window(WIN, game_assets_lib.SPACE_TRANSFORMED, 
        toDraw)

    pygame.quit()


if __name__ == "__main__":
    main()