import pygame
from utilities.drawable import displayImage
from utilities.drawable import get_text
from utilities.drawable import displayText
from utilities.drawable import displayTextButton
from classes.player import Player
from classes.enemy import Enemy
from classes.position import Position
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
        self.actionSelected = False
        self.arrowMenuPosition = Position.TOPLEFT


    def run(self):
        pygame.init()
        pygame.display.set_caption(self.gameName)

        while not self.gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gameOver = True
                self.keyEvents(event)

            self.screen.fill((0, 0, 0))
            self.buildGUI(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()

    def keyEvents(self, event):
        if event.type == 3:
            #key down
            if event.key == 274:
                if self.arrowMenuPosition == Position.TOPLEFT:
                    self.arrowMenuPosition = Position.BOTTOMLEFT
                elif self.arrowMenuPosition == Position.TOPRIGHT:
                    self.arrowMenuPosition = Position.BOTTOMRIGHT
            #key up
            elif event.key == 273:
                if self.arrowMenuPosition == Position.BOTTOMLEFT:
                    self.arrowMenuPosition = Position.TOPLEFT
                elif self.arrowMenuPosition == Position.BOTTOMRIGHT:
                    self.arrowMenuPosition = Position.TOPRIGHT
            #key left
            elif event.key == 276:
                if self.arrowMenuPosition == Position.TOPRIGHT:
                    self.arrowMenuPosition = Position.TOPLEFT
                elif self.arrowMenuPosition == Position.BOTTOMRIGHT:
                    self.arrowMenuPosition = Position.BOTTOMLEFT
            #key right
            elif event.key == 275:
                if self.arrowMenuPosition == Position.TOPLEFT:
                    self.arrowMenuPosition = Position.TOPRIGHT
                elif self.arrowMenuPosition == Position.BOTTOMLEFT:
                    self.arrowMenuPosition = Position.BOTTOMRIGHT
            #key enter
            elif event.key == 13:
                self.playAction()

    def buildGUI(self, view):
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

        #Menu arrow
        self.drawArrowMenu(view)

    def playAction(self):
        if self.arrowMenuPosition == Position.TOPLEFT:
            print("Attack")
        elif self.arrowMenuPosition == Position.TOPRIGHT:
            print("heal")
        elif self.arrowMenuPosition == Position.BOTTOMLEFT:
            print("armor")
        elif self.arrowMenuPosition == Position.BOTTOMRIGHT:
            self.exitGame()

    def exitGame(self):
        self.gameOver = True
    def drawButtons(self, view):
        #attack button
        self.drawButton(view,'ATTACK', 65, 533, 'assets/ui/button.png')

        #heal button
        self.drawHealButton(view)

        #armor button
        self.drawArmorButton(view)

        #exit button
        self.drawButton(view,'EXIT', 450, 618, 'assets/ui/button.png')

    def drawButton(self, view, text, x, y, buttonSprite, textColor = (255, 255, 255)):
        displayImage(view, buttonSprite, x, y)
        displayTextButton(view, text, x, y, textColor)

    def drawHealButton(self, view):
        textColor = (255, 255, 255) if self.player.canHeal() else (149, 129, 115)
        buttonSprite = 'assets/ui/button.png' if self.player.canHeal() else 'assets/ui/button_disable.png'

        self.drawButton(view, 'HEAL(50C)', 450, 533, buttonSprite, textColor)

    def drawArmorButton(self, view):
        textColor = (255, 255, 255) if self.player.canAddArmor() else (149, 129, 115)
        buttonSprite = 'assets/ui/button.png' if self.player.canAddArmor() else 'assets/ui/button_disable.png'
        armorCost = self.player.getArmorCost()
        buttonText = 'ARMOR('+str(armorCost)+'C)' if self.player.armor < self.player.MAX_ARMOR else 'MAX ARMOR'

        self.drawButton(view, buttonText, 65, 618, buttonSprite, textColor)

    def drawPlayerInfo(self, view):
        #heal Poins
        lifePercent = self.getPercentPoints(self.player.health, self.player.healthMax, 460)
        pygame.draw.rect(view, (255,0,0), (50, 405, lifePercent, 49))

        #heal GUI
        displayImage(view, 'assets/ui/hp_bar.png', 30, 405)

        #experience points
        expPercent = self.getPercentPoints(self.player.level.experience, self.player.level.experienceNextLevel, 336)
        pygame.draw.rect(view, (255,192,0), (65, 30, expPercent, 10))

        #experience GUI
        displayImage(view, 'assets/ui/experience.png', 10, 10)

        #level
        displayTextButton(view, str(self.player.level.level), 22, 22, width=25, height=25, fontSize=30)

        #money
        moneyStrSizes = get_text(str(self.player.money), (255, 255, 255), 45).get_rect()
        displayText(view, str(self.player.money), (900-moneyStrSizes.width-20), 20)
        displayImage(view, 'assets/ui/coin.png', (900 - moneyStrSizes.width - 78), 15)

        #round
        roundStrSizes = get_text(str(self.roundNumber), (255, 255, 255), 45).get_rect()
        displayText(view, str(self.roundNumber), (900-roundStrSizes.width-20), 80)
        displayImage(view, 'assets/ui/kills.png', (900 - roundStrSizes.width - 78), 75)

    def drawArrowMenu(self, view):
        if self.arrowMenuPosition == Position.TOPLEFT:
            displayImage(view, 'assets/ui/menu_arrow.png', 42, 540)
        elif self.arrowMenuPosition == Position.TOPRIGHT:
            displayImage(view, 'assets/ui/menu_arrow.png', 430, 540)
        elif self.arrowMenuPosition == Position.BOTTOMLEFT:
            displayImage(view, 'assets/ui/menu_arrow.png', 42, 628)
        elif self.arrowMenuPosition == Position.BOTTOMRIGHT:
            displayImage(view, 'assets/ui/menu_arrow.png', 430, 628)


    def getPercentPoints(self, points, maxPoints, maxPercent):
        if points <= 0:
            return 0
        else:
            points = (points*maxPercent)/maxPoints
            return int(points)

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
