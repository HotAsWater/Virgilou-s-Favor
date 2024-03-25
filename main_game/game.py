import pygame
from pygame.locals import *
import sys
import player
import red_platform
import bullet
from utils import constants, sound_player
import box_spawner

pygame.init()

ACC = 0.5
FRIC = -0.12


class Game:
    def __init__(self, main):
        self.main = main
        self.all_sprites = pygame.sprite.Group()
        self.boxSpawner = box_spawner.BoxSpawner(self.main)
        self.pause = False

    def game(self):
        self.main.displaySurface = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))

        pygame.display.set_caption("Virgilou's Favor")

        PT1 = red_platform.getPlatform()
        P1 = player.getPlayer(self.main)

        self.all_sprites.add(PT1)
        self.all_sprites.add(P1)

        player_shoot_cooldown = self.main.cooldownManager.add_cooldown("player_shoot")
        pause_trigger_cooldown = self.main.cooldownManager.add_cooldown("pause_menu_trigger")

        def checkBulletsInBox():
            for box_ in self.boxSpawner.getBoxes():
                for bullet_ in P1.getAllBullets():
                    if bullet_.rect.colliderect(box_.rect):
                        sound_player.play_sound("assets/sounds/explode.mp3", volume=0.1, channel=2)
                        box_.explode()
                        self.boxSpawner.getBoxes().remove(box_)
                        self.boxSpawner.play_animation.append(box_)
                        bullet_.disappear()
                        self.main.score += 1

        sound_player.play_sound("assets/sounds/background_music.mp3", volume=0.5, channel=1, loop=-1)

        background_surface = pygame.image.load("assets/images/background.png")
        background_surface = pygame.transform.scale(background_surface, (450, 600))

        while self.main.isGame():

            for event in pygame.event.get():
                keys = pygame.key.get_pressed()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if not self.pause:
                    if keys[K_SPACE]:
                        if not player_shoot_cooldown.is_on_cooldown():
                            P1.shoot()
                            player_shoot_cooldown.set_cooldown(0.5)
                if keys[K_ESCAPE]:
                    if not pause_trigger_cooldown.is_on_cooldown():
                        self.pause = not self.pause
                        pause_trigger_cooldown.set_cooldown(0.1)

            self.main.displaySurface.fill((0, 0, 0))
            self.main.displaySurface.blit(background_surface, background_surface.get_rect())

            if not self.pause:
                P1.move()
                self.boxSpawner.loop()

            for bull in P1.getAllBullets():
                if not self.pause:
                    bull.up()
                self.main.displaySurface.blit(bullet.getBullets(), bull.pos)

            for box_ in self.boxSpawner.getBoxes():
                if not self.pause:
                    box_.down()
                self.main.displaySurface.blit(box_.surf, box_.pos)

            for explosion in self.boxSpawner.play_animation:
                explosion.explode()

            for entity in self.all_sprites:
                self.main.displaySurface.blit(entity.surf, entity.rect)

            constants.showText(str(self.main.score), (400, 20), self.main.displaySurface, fontSize=24,
                               color=(10, 10, 10), font="assets/fonts/Lasting Sketch.ttf")

            if not self.pause:
                checkBulletsInBox()

            if self.pause:
                self.main.pause_menu.menu()

            pygame.display.update()
            constants.FramePerSec.tick(constants.FPS)
