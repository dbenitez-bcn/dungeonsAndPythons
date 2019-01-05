from classes.entity import Entity

class Enemy(Entity):
    def __init__(self, health, name, attackPoints, x, y, sprite, moneyWhenDying, experienceWhenDying):
        super().__init__(health, name, attackPoints, x, y, sprite)
        self.moneyWhenDying = moneyWhenDying
        self.experienceWhenDying = experienceWhenDying

    def upgradeStatsAcordingLevel(self, level):
        upgradePoints = (level/100)+1.5

        self.health *= upgradePoints
        self.health = int(self.health)

        self.healthMax *= upgradePoints
        self.healthMax = int(self.healthMax)

        self.attackPoints *= upgradePoints
        self.attackPoints = int(self.attackPoints)

        self.moneyWhenDying *= upgradePoints
        self.moneyWhenDying = int(self.moneyWhenDying)

        self.experienceWhenDying *= upgradePoints
        self.experienceWhenDying = int(self.experienceWhenDying)

    def attack(self, enemigo):
        damageMitigation = 0.08 * enemigo.armor
        finalAttackPoints = self.attackPoints*(1.0 - damageMitigation)
        enemigo.health -= int(finalAttackPoints)