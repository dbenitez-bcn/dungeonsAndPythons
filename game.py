import pygame
from utilities.drawable import displayImage
from utilities.drawable import displayText
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
        self.roundNumber = 0
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
        self.currentEnemy = self.getRandomRegularEnemy()


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
        displayImage(view, 'assets/recources/bg.png', 0, 0)

        #bottom panel
        displayImage(view, 'assets/recources/panel.png', 0, 475)

        #palyer
        self.player.draw(view)

        #enemy
        self.currentEnemy.draw(view)

        #buttons
        self.drawButtons(view)

        #Player information
        self.drawPlayerInfo(view)


    def drawButtons(self, view):
        #attack button
        displayImage(view, 'assets/ui/button.png', 165, 533)
        displayText(view, 'ATTACK', 220, 553)

        #heal button
        displayImage(view, 'assets/ui/button.png', 450, 533)
        displayText(view, 'HEAL', 540, 553)

        #armor button
        displayImage(view, 'assets/ui/button.png', 165, 618)
        displayText(view, 'ARMOR', 220, 638)

        #exit button
        displayImage(view, 'assets/ui/button.png', 450, 618)
        displayText(view, 'EXIT', 540, 638)


    def drawPlayerInfo(self, view):
        #heal points
        displayImage(view, 'assets/ui/hp_bar.png', 30, 405)
        #todo draw red rrect for the life level

        #experience
        displayImage(view, 'assets/ui/experience.png', 10, 10)
        # todo draw red rect for the exp level


    def nextRound(self):
        self.roundNumber += 1
        self.setCurrentEnemy()


    def setCurrentEnemy(self):
        if self.roundNumber % 10:
            self.currentEnemy = self.getBossEnemy()
        else:
            self.currentEnemy = self.getRandomRegularEnemy()

        self.currentEnemy.upgradeStatsAcordingLevel(self.roundNumber)


    def getRandomRegularEnemy(self):
        randomIndex = random.randint(0, len(self.enemies)-1)
        enemy = self.enemies[randomIndex]

        return enemy


    def getBossEnemy(self):
        enemy = self.boss

        return enemy
