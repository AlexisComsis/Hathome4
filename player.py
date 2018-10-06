import pygame
from tools import *

class Player(pygame.sprite.Sprite):

    def __init__(self, bank):
        pygame.sprite.Sprite.__init__(self)
        self.image = bank[0]
        self.rect = self.image.get_rect()
        self.rect.center = (tools.w0 / 2 - self.rect.width, tools.h0 / 2 - self.rect.height)
        self.speed = 1

    def update(self, window, keys, mouse, click):
        window.blit(self.image,(self.rect.center))

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()

    def update(self, window, keys, mouse, click):
        window.blit(self.image,(500, 500))
