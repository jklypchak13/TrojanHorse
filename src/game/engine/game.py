import pygame
import sys
from game.style import color as cval
from game.style import text

from .player import Player


def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


def game(screen, main_clock):
    running = True

    print("FROM GAME: running =", running)
    player = Player((0, 400, 50, 50), "path_to_player_image")

    while running:
        running = True

        screen.fill(cval.black)

        draw_text("game", text.default_font, cval.white, screen, 20, 20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_RIGHT:
                    player.right()
                if event.key == pygame.K_SPACE:
                    player.jump()

            player.draw(screen)
            pygame.display.update()
        pygame.display.update()
        main_clock.tick(60)

    print("FROM GAME: running =", running)

    return
