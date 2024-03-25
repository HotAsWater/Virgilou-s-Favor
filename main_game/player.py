import pygame
from pygame.locals import *
import bullet
import random
from utils import constants, sound_player

players = pygame.image.load("assets/images/player.jpg")
players = pygame.transform.scale(players, (50, 50))

shoot_indexes = [1, 2, 3, 4, 5, 6]

ACC = 1
FRIC = -0.12


def playRandomShoot():
    index = random.choice(shoot_indexes)
    sound_player.play_sound("assets/sounds/shoot/piou" + str(index) + ".wav", volume=0.3, channel=0)


class Player(pygame.sprite.Sprite):
    def __init__(self, main):
        super().__init__()

        self.surf = players
        self.rect = self.surf.get_rect()

        self.pos = constants.vec((constants.WIDTH / 2 - (25 / 2), constants.HEIGHT - 70))
        self.vel = constants.vec(0, 0)
        self.acc = constants.vec(0, 0)

        self.all_bullet = []

        self.main = main

    def move(self):
        self.acc = constants.vec(0, 0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > constants.WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = constants.WIDTH

        self.rect.midbottom = self.pos

    def shoot(self):
        bull = bullet.getBullet(self, self.main)
        bull.pos.x = self.pos.x - 10
        bull.pos.y = self.pos.y - 90
        self.main.displaySurface.blit(bullet.getBullets(), (self.pos.x - 10, self.pos.y - 90))
        self.getAllBullets().append(bull)
        playRandomShoot()

    def getAllBullets(self):
        return self.all_bullet


def getPlayer(main):
    P1 = Player(main)
    return P1
