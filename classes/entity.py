from utilities.drawable import displayImage
from classes.health import Health

class Entity:
    def __init__(self, health, name, attackPoints, x, y, sprite):
        self.health = Health(health)
        self.name = name
        self.attackPoints = attackPoints
        self.x = x
        self.y = y
        self.sprite = sprite

    def getHealth(self):
        return self.health.getHealth()

    def getHealthMax(self):
        return self.health.getHealthMax()

    def receiveDamage(self, damagePoints):
        self.health.receiveDamage(damagePoints)

    def isDead(self):
        return self.health.isDead()

    def draw(self, view):
        displayImage(view, self.sprite, self.x, self.y)