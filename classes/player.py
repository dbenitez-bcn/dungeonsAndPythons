from classes.entity import *
from classes.level import *
import random
class Player(Entity):
    def __init__(self, health, name, attackPoints, x, y, sprite):
        super().__init__(health, name, attackPoints, x, y, sprite)
        self.armor = 0
        self.MAX_ARMOR = 5
        self.money = 0
        self.level = Level()

    def canHeal(self):
        if (self.money > 20) & (self.health < self.healthMax):
            return True
        else:
            return False

    def heal(self):
        if self.canHeal():
            self.money -= 20
            self.health += 50

    def canAddArmor(self):
        if self.armor < self.MAX_ARMOR:
            return True
        else:
            return False

    def addArmor(self):
        if self.canAddArmor():
            self.armor += 1

    def levelUp(self):
        self.level.levelUp()
        self.upgradeStats()

    def upgradeStats(self):
        healPoints = self.getUpgradePoints(10, 15)
        self.healthMax += healPoints
        self.health += healPoints

        self.attackPoints += self.getUpgradePoints(1, 3)

    def getUpgradePoints(self, min, max):
        return random.randint(min,max)