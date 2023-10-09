import os 

import pygame 

ASSETS_DIR = os.path.join('..', 'assets')
FONTS_DIR = os.path.join(ASSETS_DIR, 'fonts')

class Score:

    def __init__(self):
        self.score = 0
        self.font = pygame.font.Font(os.path.join(FONTS_DIR, 'flappy-font.ttf'), 60)
        self.text = self.font.render(str(self.score), True, (0, 0, 0))
        self.text_rect = self.text.get_rect()
        self.text_rect.center = (100, 20)

    def update_score(self, score_change):
        self.score += score_change

    def update(self):
        self.text = self.font.render(str(self.score), True, (0, 0, 0))

    def draw(self, screen):
        screen.blit(self.text, (200, 40))