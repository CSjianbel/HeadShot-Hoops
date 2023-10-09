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
        self.move_speed = 5

    def move_left(self):
        self.rect.x += -self.move_speed
    
    def move_right(self):
        self.rect.x += self.move_speed 


