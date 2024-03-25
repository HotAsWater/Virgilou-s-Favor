import pygame
import random
from utils import constants

box_surface = pygame.image.load("assets/images/boxAlt.png")
box_surface = pygame.transform.scale(box_surface, (50, 50))

FRIC = -0.1

explosions = []
explosions_i = 0


def load_explodes():
    for i in range(1, 11):
        explode_surface = pygame.image.load("assets/images/explodes/Explosion_"+str(i)+".png")
        explode_surface = pygame.transform.scale(explode_surface, (75, 75))
        explosions.append(explode_surface)


class Box(pygame.sprite.Sprite):
    def __init__(self, main):
        super().__init__()

        self.surf = box_surface
        self.rect = self.surf.get_rect()

        randX = random.randrange(0, constants.WIDTH, 50)

        self.pos = constants.vec((randX, -50))
        self.vel = constants.vec(0, 0)
        self.acc = constants.vec(0, 0)

        self.ACC = 0.2 + random.uniform(0, main.settings.difficulty) / (2 * int(main.settings.difficulty+1))

        self.main = main

        self.rect = pygame.Rect(self.pos.x, self.pos.y, 50, 50)
        self.main.displaySurface.blit(box_surface, self.pos)
        load_explodes()

    def down(self):

        if self.pos.y >= constants.HEIGHT - 70:
            self.main.gameEnd()
        else:
            self.acc.y = self.ACC

            self.acc.y += self.vel.y * (FRIC/abs(self.main.settings.difficulty-2.5))
            self.vel += self.acc
            self.pos += self.vel + 0.5 * self.acc

            self.rect.update(self.pos.x, self.pos.y, 50, 50)

    def explode(self):
        global explosions_i
        explosion_rect = pygame.Rect(self.pos.x - 75/4, self.pos.y - 75 / 4, 75, 75)
        self.main.displaySurface.blit(explosions[int(explosions_i)], explosion_rect)

        explosions_i += 0.5
        if explosions_i == 9:
            explosions_i = 0
            self.main.game_.boxSpawner.play_animation.remove(self)
