import pygame.mixer
from pygame import mixer


def play_sound(path="", volume=1, channel=0, loop=0):
    mixer.init(channels=10)
    sound = pygame.mixer.Sound(path)
    sound.set_volume(volume)
    mixer.Channel(channel).play(sound, loops=loop)
