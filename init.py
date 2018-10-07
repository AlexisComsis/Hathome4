from data_init import *
import pygame


# [WINDOW]
window = pygame.display.set_mode((Info.w0, Info.h0), pygame.FULLSCREEN)

pygame.display.set_icon(Info.icon)
pygame.display.set_caption("HatHome")

# [MUSIC]
pygame.mixer.music.load("Assets\Music\Farm.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(Info.volume)

clock = pygame.time.Clock()

# OBJECT
