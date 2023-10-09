import pygame

from game.utils.window import Window
from game.entities.basket import Basket
from game.entities.falling_item import FallingItem
from game.entities.score import Score
from game.utils.sprites import Sprites

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('HeadShot Hoops')
        self.clock = pygame.time.Clock()
        self.window = Window(600, 800)
        self.fps = 60
        self.screen = pygame.display.set_mode((self.window.width, self.window.height))
        self.running = True
        self.sprites = Sprites()
        self.falling_items = pygame.sprite.Group()
        self.net = Basket(self.sprites.net)
        self.net_group = pygame.sprite.GroupSingle()
        self.net_group.add(self.net)
        self.item_frequency = 1000
        self.last_item = pygame.time.get_ticks() - self.item_frequency
        self.score = Score()

    def generate_items(self):
        time_now = pygame.time.get_ticks()
        if time_now - self.last_item > self.item_frequency:
            self.falling_items.add(FallingItem(self.sprites.ball, True))
            self.last_item = time_now
        self.falling_items.update()

    # def check_basket_collisions(self):
    #     if pygame.sprite.groupcollide(self.net_group, self.falling_items, False, False):
    #         self.score.update_score()


    def start(self):
        
        while self.running:
            keys = pygame.key.get_pressed()

            if keys[pygame.K_LEFT]:
                self.net.move_left()
            elif keys[pygame.K_RIGHT]:
                self.net.move_right()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            self.screen.fill((255, 255, 255))
            self.generate_items()
            self.falling_items.draw(self.screen)
            self.net_group.draw(self.screen)
            self.falling_items.update()
            self.net_group.update()

            self.clock.tick(self.fps)

            pygame.display.update()

def main():
    game = Game()
    game.start()

if __name__ == '__main__':
    main()

