import pygame
import os

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
            self.buildUI()
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def get_image(self, path):
        self._image_library
        image = self._image_library.get(path)
        if image == None:
            canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
            image = pygame.image.load(canonicalized_path)
            self._image_library[path] = image
        return image

    def buildUI(self):
        self.screen.blit(self.get_image('assets/recources/bg.png'), (0, 0))
        self.screen.blit(self.get_image('assets/recources/panel.png'), (0, 476))
