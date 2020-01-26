from utilities.drawable import displayImage

class Armor:
    def __init__(self):
        self.__armor = 0
        self.__MAX_ARMOR = 5

    
    def canAddArmor(self):
        if (self.__armor < 5):
            return True
        else:
            return False
    
    def getArmor(self):
        return self.__armor

    def getArmorCost(self):
        return 150 + (50 * self.__armor)

    def addArmor(self):
        self.__armor += 1

    def haveMaxArmor(self):
        if self.__armor < self.__MAX_ARMOR:
            return False
        else:
            return True

    def drawArmor(self, view):
        if self.__armor > 0:
            displayImage(view, 'assets/ui/armor.png', 480, 350)
        if self.__armor > 1:
            displayImage(view, 'assets/ui/armor.png', 428, 350)
        if self.__armor > 2:
            displayImage(view, 'assets/ui/armor.png', 376, 350)
        if self.__armor > 3:
            displayImage(view, 'assets/ui/armor.png', 324, 350)
        if self.__armor > 4:
            displayImage(view, 'assets/ui/armor.png', 272, 350)