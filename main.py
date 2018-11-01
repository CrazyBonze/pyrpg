import time
import pygame
import logging
from configparser import ConfigParser
from config import Config
from game import Game


def main():
    pygame.init()
    surface_sz = 480

    main_surface = pygame.display.set_mode(
        (surface_sz, surface_sz),
        pygame.HWSURFACE | pygame.DOUBLEBUF)

    small_rect = (300, 200, 150, 90)
    some_color = (255, 0, 0)

    while True:

        # Handle events
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break

        # Update game state
        # TODO

        # Draw surface
        main_surface.fill((0, 200, 255))
        main_surface.fill(some_color, small_rect)

        # Show surface
        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    config = Config()
    logging.basicConfig(level=logging.INFO)
    g = Game(debug=config['DEFAULT'].getboolean('debug'))
    g.run()
