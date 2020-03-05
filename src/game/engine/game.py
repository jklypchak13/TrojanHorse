import pygame  # type: ignore
import sys
from game.style import color as cval  # type: ignore
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
    player = Player(pygame.Rect(0, 400, 50, 50), "path_to_player_image")
    obstacles = [Obstacle(pygame.Rect(400, 400, 50, 50), "path_to_obstacle_image")]
    screen_offset = [0,0]
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
                if event.key in player.controls:
                    player.controls[event.key]()

        # Check collisions
        for obstacle in obstacles:
            if player.is_collided_with(obstacle):
                print("Collided")

        #Recalculate screen_offset
        w, h = pygame.display.get_surface().get_size()
        if player.position.x+screen_offset[0]<20:
            screen_offset[0]=20-player.position.x
        if player.position.right+screen_offset[0]>w-20:
            screen_offset[0]=w-20-player.position.right
        #Redraw screen
        player.draw(screen,screen_offset)
        for obstacle in obstacles:
            obstacle.draw(screen,screen_offset)
        pygame.display.update()

        main_clock.tick(60)

    print("FROM GAME: running =", running)

    return
