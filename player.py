import pygame
from tools import *

class Player(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((64,64))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        self.rect.center = (tools.w0 / 2, tools.h0 / 2)
        self.speed = 1

    def update(self, window, keys, mouse, click):
        self.image.pygame.Surface.blit(window,self.rect.center)
