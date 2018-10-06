from tools import *
import pygame


# [WINDOW]
window = pygame.display.set_mode((tools.w0, tools.h0), pygame.FULLSCREEN)

from load import *
from player import *

pygame.display.set_icon(icon)
pygame.display.set_caption("HatHome")

# [MUSIC]
pygame.mixer.music.load("Assets\Music\music.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(4)

clock = pygame.time.Clock()

# OBJECT
all_sprites = pygame.sprite.Group()
home = Player()
all_sprites.add(home)
