import pygame
from drawable import draw
from classes.player import Player
from classes.enemy import Enemy
import random

class Game:
    def __init__(self):
        self.gameName = "Dungeons & Pythons"
        self._image_library = {}
        self.screen = pygame.display.set_mode((900, 750))
        self.gameOver = False
        self.clock = pygame.time.Clock()
        self.roundNumber = 1
        self.player = Player(100, "Hero", 25, 50, 125, "assets/player/player.png")
        self.boss = Enemy(100, "The BOSS: Dragon", 20, 550, 100, "assets/monsters/boss.png", 300, 200)
        self.enemies = [Enemy(50, "Cloud ashes", 10, 550, 100, "assets/monsters/ashesSnake.png", 50, 10),
                        Enemy(50, "Yaretzi", 15, 550, 100, "assets/monsters/aztecaSnake.png", 50, 15),
                        Enemy(40, "Konoha", 7, 550, 100, "assets/monsters/fireFairy.png", 40, 10),
                        Enemy(35, "Fire spliter", 10, 550, 100, "assets/monsters/fireLizard.png", 35, 10),
                        Enemy(40, "Duchy", 7, 550, 100, "assets/monsters/groundFairy.png", 40, 10),
                        Enemy(45, "Medusa's daughter", 13, 550, 100, "assets/monsters/groundSnake.png", 45, 13),
                        Enemy(40, "Imperial", 12, 550, 100, "assets/monsters/imperialBird.png", 40, 12),
                        Enemy(35, "Scissors", 9, 550, 100, "assets/monsters/scorpio.png", 35, 10),
                        Enemy(20, "Awesome bats", 8, 550, 100, "assets/monsters/triBats.png", 20, 10),
                        Enemy(45, "Hydra", 14, 550, 100, "assets/monsters/triHead.png", 45, 14),
                        Enemy(25, "The python brothers", 5, 550, 100, "assets/monsters/triSnakes.png", 25, 10),
                        Enemy(40, "Amega", 7, 550, 100, "assets/monsters/waterFairy.png", 40, 7)]
        self.currentEnemy = self.getCurrentEnemy()

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

        #palyer
        self.player.draw(view)

        #enemy
        self.currentEnemy.draw(view)

    def getCurrentEnemy(self):
        randomIndex = random.randint(1, len(self.enemies)-1)

        enemy = self.enemies[randomIndex]
        enemy.upgradeStatsAcordingLevel(self.roundNumber)

        return enemy

