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
        enemigo.health -= self.attackPoints

    def isDead(self):
        if self.health < 0:
            return True
        else:
            return False

    def draw(self):
        print("TODO implement how to dra    w")