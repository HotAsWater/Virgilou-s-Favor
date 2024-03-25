import pygame
from utils import constants

bullets = pygame.image.load("assets/images/bullet.jpg")
bullets = pygame.transform.scale(bullets, (20, 40))


ACC = 1.5
FRIC = -0.25


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player,main):
        super().__init__() 
        
        self.surf = bullets
        self.rect = self.surf.get_rect()
        
        self.pos = constants.vec((10, 385))
        self.vel = constants.vec(0, 0)
        self.acc = constants.vec(0, 0)
        
        self.player = player
        self.main = main
        self.rect = pygame.Rect(self.pos.x, self.pos.y, 20, 40)

    def up(self):
        self.acc.y = -ACC
    
        self.acc.y += self.vel.y * FRIC
        self.vel += self.acc
        self.pos += self.vel + -0.5 * self.acc

        self.rect.update(self.pos.x, self.pos.y, 20, 40)
        
        if self.pos.y <= -40:
            self.disappear()
        
    def disappear(self):
        self.player.getAllBullets().remove(self)


def getBullet(player, main):
    return Bullet(player, main)   


def getBullets():
    return bullets
    
        


