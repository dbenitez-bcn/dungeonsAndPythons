from classes.entity import Entity

class Enemy(Entity):
    def __init__(self, health, name, attackPoints, x, y, sprite, moneyWhenDying, experienceWhenDying):
        super().__init__(health, name, attackPoints, x, y, sprite)
        self.moneyWhenDying = moneyWhenDying
        self.experienceWhenDying = experienceWhenDying

    def upgradeStatsAcordingLevel(self, level):
        upgradePoints = self.getUpgradePoints(level)

        self.health.upgradeEnemyStats(upgradePoints)

        self.attackPoints *= upgradePoints
        self.attackPoints = int(self.attackPoints)

        self.moneyWhenDying *= upgradePoints
        self.moneyWhenDying = int(self.moneyWhenDying)

        self.experienceWhenDying *= upgradePoints
        self.experienceWhenDying = int(self.experienceWhenDying)

    def getUpgradePoints(self, level):
        return (level/100)+1.5

    def attack(self, enemigo):
        finalAttackPoints = self.attackPoints*(1.0 - enemigo.damageMitigation())
        enemigo.receiveDamage(int(finalAttackPoints))