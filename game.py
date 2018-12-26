import pygame
from drawable import draw

class Game:
    def __init__(self):
        self.gameName = "Dungeons & Pythons"
        self._image_library = {}
        self.screen = pygame.display.set_mode((900, 750))
        self.gameOver = False
        self.clock = pygame.time.Clock()

    def run(self):
        pygame.init()
        pygame.display.set_caption(self.gameName)

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True

            self.screen.fill((0, 0, 0))
            self.buildUI(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()



    def buildUI(self, view):
        #background
        draw(view, 'assets/recources/bg.png', 0, 0)
        #bottom panel
        draw(view, 'assets/recources/panel.png', 0, 476)

