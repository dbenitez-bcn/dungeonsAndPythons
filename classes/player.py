import random
from classes.entity import *
from classes.level import *
from classes.armor import Armor

class Player(Entity):
    def __init__(self, health, name, attackPoints, x, y, sprite):
        super().__init__(health, name, attackPoints, x, y, sprite)
        self.armor = Armor()
        self.money = 0
        self.level = Level()

    def canHeal(self):
        if (self.money >= 20) & (self.health.canHeal()):
            return True
        else:
            return False

    def heal(self):
        if self.canHeal():
            self.money -= 20
            self.health.heal()

    def canAddArmor(self):
        if (self.armor.canAddArmor()) & (self.money >= self.armor.getArmorCost()):
            return True
        else:
            return False

    def haveMaxArmor(self):
        return self.armor.haveMaxArmor()

    def getArmorCost(self):
        return self.armor.getArmorCost()

    def addArmor(self):
        if self.canAddArmor():
            self.armor.addArmor()

    def damageMitigation(self):
        return 0.08 * self.armor.getArmor()

    def levelUp(self):
        self.level.levelUp()
        self.upgradeStats()

    def upgradeStats(self):
        healUpgradePoints = self.getUpgradePoints(10, 15)
        self.health.upgradeStats(healUpgradePoints)

        self.attackPoints += self.getUpgradePoints(1, 3)

    def getUpgradePoints(self, min, max):
        return random.randint(min,max)

    def attack(self, enemigo):
        enemigo.receiveDamage(self.attackPoints)
    
    def drawArmor(self, view):
        self.armor.drawArmor(view)