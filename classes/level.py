class Level:
    def __init__(self):
        self.level = 1
        self.experience = 0
        self.experienceNextLevel = 50

    def addExperience(self, expPoints):
        self.experience += expPoints
        if self.canLevelUp():
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.experience -= self.experienceNextLevel
        self.experienceNextLevel *= 1.4
        if self.canLevelUp():
            self.levelUp()

    def canLevelUp(self):
        if self.experience > self.experienceNextLevel:
            return True
        else:
            return False
