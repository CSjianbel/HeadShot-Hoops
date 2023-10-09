import pygame

from game.utils.window import Window
from game.entities.basket import Basket
from game.entities.falling_item import FallingItem
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
        self.ball = FallingItem(self.sprites.ball, True)
        self.ball_group = pygame.sprite.Group()
        self.net = Basket(self.sprites.net)
        self.net_group = pygame.sprite.GroupSingle()
        self.ball_group.add(self.ball)
        self.net_group.add(self.net)

    def start(self):
        
        self.screen.fill((255, 255, 255))
        while self.running:
            self.ball_group.draw(self.screen)
            self.net_group.draw(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.clock.tick(self.fps)

            pygame.display.update()

def main():
    game = Game()
    game.start()

if __name__ == '__main__':
    main()

