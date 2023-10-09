import random

import pygame

# Inherit this class for all falling items
class FallingItem(pygame.sprite.Sprite):

    def __init__(self, sprite, valid: bool):
        pygame.sprite.Sprite.__init__(self)
        self.screen_dim = pygame.display.get_surface().get_size()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = [
            random.randint(self.rect.w, self.screen_dim[0] - self.rect.w),
            self.rect.h // 2
        ]
        self.fall_speed = 0.2
        # Boolean that represents if item should be caught by basket or not
        self.valid = valid

    def score(self):
        return 1 if self.valid else -1

    def fall(self):
        self.rect.y += self.fall_speed
    
    def update(self):
        self.fall()
        if self.rect.y > self.screen_dim[1]:
            self.kill()