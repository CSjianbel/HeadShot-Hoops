import pygame 

class Basket(pygame.sprite.Sprite):

    def __init__(self, sprite):
        pygame.sprite.Sprite.__init__(self)
        self.screen_dim = pygame.display.get_surface().get_size()
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.center = [
            self.screen_dim[0] // 2,
            self.screen_dim[1] - (self.rect.h // 2),
        ]

    def update(self):
        pass

