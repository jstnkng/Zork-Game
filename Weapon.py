class Weapon:
    def __init__ (self, Name, maxDamage, minDamage, Uses):
        self.Name = Name
        self.maxDamage = maxDamage
        self.minDamage = minDamage
        self.Uses = Uses
        
    def getUses(self):
        return self.Uses

    def useWeapon(self):
        self.Uses = self.Uses - 1

    def getMinDamage(self):
        return self.minDamage
    
    def getMaxDamage(self):
        return self.maxDamage

class HersheysKiss(Weapon):
    def __init__ (self, Name="HersheysKiss", maxDamage=100, minDamage=100, Uses=99):
        super(HersheysKiss, self).__init__(Name, maxDamage, minDamage, Uses)

class SourStraw(Weapon):
    def __init__ (self, Name="SourStraw", maxDamage=175, minDamage=100, Uses=2):
        super(SourStraw, self).__init__(Name, maxDamage, minDamage, Uses)

class ChocolateBar(Weapon):
    def __init__ (self, Name="ChocolateBar", maxDamage=240, minDamage=200, Uses=4):
        super(ChocolateBar, self).__init__(Name, maxDamage, minDamage, Uses)

class NerdBomb(Weapon):
    def __init__ (self, Name="NerdBomb", maxDamage=500, minDamage=350, Uses=1):
        super(NerdBomb, self).__init__(Name, maxDamage, minDamage, Uses)
