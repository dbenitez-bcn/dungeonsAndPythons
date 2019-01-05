from utilities.drawable import displayImage

class Entity:
    def __init__(self, health, name, attackPoints, x, y, sprite):
        self.health = health
        self.healthMax = health
        self.name = name
        self.attackPoints = attackPoints
        self.x = x
        self.y = y
        self.sprite = sprite

    def attack(self, enemigo):
        if enemigo is Enemy:
            enemigo.health -= self.attackPoints
        else:
            damageMitigation = 0.08 * enemigo.armor
            finalAttackPoints = self.attackPoints*damageMitigation
            print("Damage mitigation->"+str(damageMitigation)+"// Final points->"+str(finalAttackPoints))
            enemigo.health -= finalAttackPoints


    def isDead(self):
        if self.health < 0:
            return True
        else:
            return False

    def draw(self, view):
        displayImage(view, self.sprite, self.x, self.y)