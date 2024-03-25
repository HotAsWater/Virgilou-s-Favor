from utils import constants, sound_player
import pygame
import sys


class StartMenu:
    def __init__(self, main):
        self.main = main

        self.menu = "main"

    def open_menu(self):
        self.main.displaySurface = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
        self.main.displaySurface.fill((0, 0, 0))
        pygame.display.flip()

        while self.main.is_start_menu:

            if self.menu == "main":
                self.main_menu()
            elif self.menu == "difficulty":
                self.difficulty_menu()
            elif self.menu == "settings":
                self.settings_menu()

            pygame.display.update()
            constants.FramePerSec.tick(constants.FPS)

    def main_menu(self):
        self.main.displaySurface.fill((40, 40, 40))

        constants.showText("Virgilou's", (constants.WIDTH / 2, constants.HEIGHT / 2 - 180), self.main.displaySurface,
                           fontSize=65, color=(255, 255, 255), font="assets/fonts/Dacherry.ttf")
        constants.showText("Favor", (constants.WIDTH / 2, constants.HEIGHT / 2 - 125), self.main.displaySurface,
                           fontSize=40, color=(255, 255, 255), font="assets/fonts/Dacherry.ttf")

        playButtonSurface = pygame.image.load("assets/images/startButton.png")
        playButtonSurface = pygame.transform.scale(playButtonSurface, (146, 60))

        pos_play = constants.vec((constants.WIDTH / 2 - playButtonSurface.get_width() / 2, constants.HEIGHT / 2 - 50))
        play_rect = pygame.Rect(pos_play.x, pos_play.y, 146, 60)

        mousePos = pygame.mouse.get_pos()

        if play_rect.collidepoint(mousePos):
            delta = play_rect.width * 1 - play_rect.width

            playButtonSurface = pygame.image.load("assets/images/startButtonHover.png")
            playButtonSurface = pygame.transform.scale(playButtonSurface, (146, 60))

            playButtonSurface = pygame.transform.smoothscale_by(playButtonSurface, 1)
            play_rect.update(pos_play.x - delta / 2, pos_play.y - delta / 4, 146, 60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_rect.collidepoint(mousePos):
                    sound_player.play_sound("assets/sounds/button_click.mp3", channel=0, volume=0.3)
                    self.menu = "difficulty"
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.main.displaySurface.blit(playButtonSurface, play_rect)

    def difficulty_menu(self):
        self.main.displaySurface.fill((40, 40, 40))

        buttons = {"hard_button": 0.4, "normal_button": 0.9, "easy_button": 1.4}
        buttons_rect = {}

        mousePos = pygame.mouse.get_pos()

        i = 0
        for buttonId, difficulty in buttons.items():
            button_surface = pygame.image.load("assets/images/"+buttonId+".png")
            button_surface = pygame.transform.scale(button_surface, (146, 60))

            pos_button = constants.vec(
                (constants.WIDTH / 2 - button_surface.get_width() / 2, constants.HEIGHT / 2 - (80 * i)))
            button_rect = pygame.Rect(pos_button.x, pos_button.y, 146, 60)

            buttons_rect[buttonId] = button_rect

            if button_rect.collidepoint(mousePos):
                button_surface = pygame.image.load("assets/images/" + buttonId + "_hover" + ".png")
                button_surface = pygame.transform.scale(button_surface, (146, 60))

            self.main.displaySurface.blit(button_surface, button_rect)

            i += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for button, difficulty in buttons.items():
                    button_rect = buttons_rect[button]
                    if button_rect.collidepoint(mousePos):
                        sound_player.play_sound("assets/sounds/button_click.mp3", channel=0, volume=0.3)
                        self.menu = "main"
                        self.main.settings.difficulty = difficulty
                        self.main.game()

    def settings_menu(self):
        pass
