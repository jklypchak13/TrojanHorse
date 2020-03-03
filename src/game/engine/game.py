import pygame
import sys
from game.style import color as cval
from game.style import text

from .player import Player
from .obstacle import Obstacle


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game(screen, main_clock):
    running = True

    print("FROM GAME: running =", running)
    player = Player(pygame.Rect(0, 400, 50, 50), 'src\assets\game\whiteSquare.png')
    obstacles = [Obstacle(pygame.Rect(400,400,50,50), "path_to_obstacle_image")]

    while running:
        running = True

        screen.fill(cval.black)

        draw_text("game", text.default_font, cval.white, screen, 20, 20)
        
        Player.updateJump(player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key in player.controls:
                    getattr(player,player.controls[event.key])()

        #Check collisions
        for obstacle in obstacles:
            if player.is_collided_with(obstacle):
                print("Collided")
        player.draw(screen)
        for obstacle in obstacles:
            obstacle.draw(screen)
        pygame.display.update()
        main_clock.tick(60)

    print("FROM GAME: running =", running)

    return
