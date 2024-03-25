import pygame
from utils import constants

platforme = pygame.image.load("assets/images/down_platform.png")

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = platforme
        self.rect = self.surf.get_rect()
        self.rect = self.surf.get_rect(center = (constants.WIDTH / 2, constants.HEIGHT - 35))
        
        
PT1 = platform()
def getPlatform():
    return PT1
