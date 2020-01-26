class Health:
    def __init__(self, health):
        self.__health = health
        self.__healthMax = health
    
    def isDead(self):
        if self.__health < 0:
            return True
        else:
            return False

    def canHeal(self):
        return self.__health < self.__healthMax

    def heal(self):
        self.__health += 50
        if self.__health > self.__healthMax:
            self.__health = self.__healthMax

    def receiveDamage(self, damagePoints):
        self.__health -= damagePoints

    def upgradeStats(self, upgradePoints):
        self.__healthMax += healPoints
        self.__health += healPoints

    def upgradeEnemyStats(self, upgradePoints):
        self.__health *= int(upgradePoints)
        self.__healthMax *= int(upgradePoints)

    def getHealth(self):
        return self.__health

    def getHealthMax(self):
        return self.__healthMax
