import pygame

FPS = 60
WIDTH, HEIGHT = 450, 600
FramePerSec = pygame.time.Clock()
vec = pygame.math.Vector2


def showText(message, position, surface, fontSize=20, color=(255, 255, 255), font=None):
    font = pygame.font.Font(font, fontSize)

    text_surf = font.render(message, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (position[0]), (position[1])
    surface.blit(text_surf, text_rect)
