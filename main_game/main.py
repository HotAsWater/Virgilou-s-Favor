import game
import over
from utils import settings
from utils import cooldown
from gui import pause_menu, start_menu
import pygame


class Main:
    def __init__(self):
        self.displaySurface = None
        self.is_start_menu = True
        self.is_game = False
        self.is_over = False
        self.game_ = None

        self.score = 0
        self.best_score = 0

        self.pause_menu = pause_menu.PauseMenu(self)
        self.settings = settings.Settings(self)
        self.cooldownManager = cooldown.CooldownManager(self)

    def startMenu(self):
        self.is_over = False
        self.is_start_menu = True
        startMenu = start_menu.StartMenu(self)
        startMenu.open_menu()

    def game(self):
        self.is_start_menu = False
        self.is_game = True
        self.game_ = game.Game(self)
        self.game_.game()

    def isGame(self):
        return self.is_game

    def isOver(self):
        return self.is_over

    def gameEnd(self):
        for entity in self.game_.all_sprites:
            self.game_.all_sprites.remove(entity)

        for box_ in self.game_.boxSpawner.getBoxes():
            self.game_.boxSpawner.getBoxes().remove(box_)

        if self.score > self.best_score:
            self.best_score = self.score

        self.is_game = False
        self.is_over = True
        over_ = over.GameOver(self)
        over_.over()

    def replay(self):
        self.is_over = False
        self.score = 0
        self.game()

    def fill(self, surface, color):
        """Fill all pixels of the surface with color, preserve transparency."""
        w, h = surface.get_size()
        r, g, b, _ = color
        for x in range(w):
            for y in range(h):
                a = surface.get_at((x, y))[3]
                surface.set_at((x, y), pygame.Color(r, g, b, a))


main = Main()
main.startMenu()
