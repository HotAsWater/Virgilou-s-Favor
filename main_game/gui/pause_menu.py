import pygame

from utils import constants


class PauseMenu:
    def __init__(self, main):
        self.main = main

    def menu(self):

        background = pygame.Surface((constants.WIDTH, constants.HEIGHT))
        background.fill((0, 0, 0), pygame.Rect(0, 0, constants.WIDTH, constants.HEIGHT))
        background.set_alpha(30)

        self.main.displaySurface.blit(background, background.get_rect())

        constants.showText("Pause", (constants.WIDTH / 2, constants.HEIGHT / 2 - 200), self.main.displaySurface,
                           fontSize=50, color=(255, 0, 100), font="assets/fonts/LEMONMILK-Light.otf")

