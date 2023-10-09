import os

import pygame

ASSETS_DIR = os.path.join('..', 'assets')
SPRITES_DIR = os.path.join(ASSETS_DIR, 'sprites')

class Sprites:
    def __init__(self):
        self.net = pygame.image.load(os.path.join(SPRITES_DIR, 'net.png'))
        self.net = pygame.transform.scale(self.net, (150,150))
        self.ball = pygame.image.load(os.path.join(SPRITES_DIR, 'ball.png'))
        self.ball = pygame.transform.scale(self. ball, (90, 90))