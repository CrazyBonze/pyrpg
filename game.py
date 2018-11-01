import sys
import time
import pygame
import logging
from os.path import join
from menue import Menue
from enum import Enum
from pygame.time import Clock
from time import time
import pygame_assets as assets

class GameState(Enum):
    INTRO = 1
    MAIN = 2
    RUNNING = 4
    PAUSED = 8

class Game():
    def __init__(
            self,
            framerate= 0,
            surface_x=272,
            surface_y=153,
            scaler=4,
            debug=True):
        logging.info("Initializing game.")
        self.framerate = framerate
        if debug:
            logging.warn("Game loading in debug mode.")
        self.surface_x = surface_x * scaler
        self.surface_y = surface_y * scaler
        self.scaler = scaler
        self.debug = debug
        pygame.init()
        self.main_surface = pygame.display.set_mode(
            (self.surface_x, self.surface_y),
            pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.clock = Clock()
        self.state = GameState.INTRO
        # self.font = pygame.font.Font(
        #     join('assets', 'font', 'Diary-of-an-8-bit-mage.woff'),
        #     16)
        # self.font = pygame.font.SysFont("Courier", 16)
        self.font = pygame.font.Font(
            join('assets', 'font', 'C&C-Red-Alert-[INET].ttf'),
            16)
        self.menue = Menue(self.main_surface, self.font)
        self.background = assets.load.image("parallax-mountain-bg.png")
        self.background = pygame.transform.scale(
            self.background,
            tuple(i * self.scaler for i in self.background.get_rect().size))

    def run(self):
        """Start the game loop."""
        while True:
            self.clock.tick(self.framerate)
            self.handle_events()
            self.update_state()
            self.display()
            #print(self.clock.get_fps())


    def handle_events(self):
        """Event handler.

        Figures out what to do from the events it polled.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if pygame.key.name(event.key) == 'escape':
                    if self.state == GameState.INTRO:
                        self.state = GameState.MAIN
                    elif self.state == GameState.PAUSED:
                        self.state = GameState.MAIN
                    elif self.state == GameState.MAIN:
                        self.state = GameState.PAUSED
                print(pygame.key.name(event.key))

    def intro(self):
        self.main_surface.blit(self.background, (0, 0))


    def update_state(self):
        if self.state == GameState.INTRO:
            self.intro()
        if self.state == GameState.MAIN:
            self.menue.draw('main')
        if self.state == GameState.PAUSED:
            self.menue.draw('paused')
        if self.state == GameState.RUNNING:
            pass

    def display_fps(self):
        fps_counter = "FPS: {0}".format(self.clock.get_fps())
        fps_rendered = self.font.render(fps_counter, True, (0, 0, 0))
        self.main_surface.blit(fps_rendered, (10, 10))

    def display(self):
        if self.debug:
            self.display_fps()
        pygame.display.flip()

    def quit(self):
        """Handle all cleanup code."""
        logging.info("Closing game.")
        pygame.quit()
        sys.exit()
