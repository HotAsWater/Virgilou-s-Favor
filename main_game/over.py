import pygame
from pygame.locals import *
import sys
from utils import constants, sound_player


class GameOver:
    def __init__(self, main):
        self.main = main

    def over(self):
        self.main.displaySurface = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.main.displaySurface.fill((0, 0, 0))
        pygame.display.flip()

        sound_player.play_sound("assets/sounds/die.mp3", volume=1, channel=1)

        while self.main.isOver():
            self.main.displaySurface.fill((40, 40, 40))

            buttonSurface = pygame.image.load("assets/images/playAgainButton.png")
            buttonSurface = pygame.transform.scale(buttonSurface, (50, 50))

            posPlayAgain = constants.vec((constants.WIDTH / 2 - 25, constants.HEIGHT / 2))

            mousePos = pygame.mouse.get_pos()
            playButtonRect = pygame.Rect(posPlayAgain.x, posPlayAgain.y, 50, 50)

            if playButtonRect.collidepoint(mousePos):
                delta = playButtonRect.width*1.1 - playButtonRect.width

                self.main.fill(buttonSurface, pygame.Color(230, 230, 230))
                buttonSurface = pygame.transform.smoothscale_by(buttonSurface, 1.1)
                playButtonRect.update(posPlayAgain.x - delta/2, posPlayAgain.y - delta/2, 50, 50)

            self.main.displaySurface.blit(buttonSurface, playButtonRect)

            mainMenuSurface = pygame.image.load("assets/images/menu_button.png")
            mainMenuSurface = pygame.transform.scale(mainMenuSurface, (97, 40))

            mainMenuPos = constants.vec((constants.WIDTH/2 - 97/2, constants.HEIGHT / 2 + 80))
            mainMenuRect = pygame.Rect(mainMenuPos.x, mainMenuPos.y, 97, 40)

            if mainMenuRect.collidepoint(mousePos):
                mainMenuSurface = pygame.image.load("assets/images/menu_button_hover.png")
                mainMenuSurface = pygame.transform.scale(mainMenuSurface, (97, 40))

            self.main.displaySurface.blit(mainMenuSurface, mainMenuRect)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if playButtonRect.collidepoint(mousePos):
                        self.replay()
                    elif mainMenuRect.collidepoint(mousePos):
                        self.main.startMenu()

            constants.showText("Perdu !", (constants.WIDTH / 2, constants.HEIGHT / 2 - 120), self.main.displaySurface,
                               fontSize=60, color=(223, 41, 53), font="assets/fonts/Dacherry.ttf")
            constants.showText("Score: " + str(self.main.score), (constants.WIDTH / 2, constants.HEIGHT / 2 - 80),
                               self.main.displaySurface, fontSize=30, color=(220, 220, 220),
                               font="assets/fonts/Lasting Sketch.ttf")

            constants.showText("Meilleur score: " + str(self.main.best_score), (
                constants.WIDTH / 2, constants.HEIGHT / 2 - 35),
                               self.main.displaySurface, fontSize=14, color=(200, 200, 200),
                               font="assets/fonts/LEMONMILK-Light.otf")

            pygame.display.update()
            constants.FramePerSec.tick(constants.FPS)

    def replay(self):
        sound_player.play_sound("assets/sounds/play_again.mp3", channel=0)
        self.main.replay()
