import random
from Observer import Observer

class NPC(Observer):
    def __init__ (self, Name, HP, maxAttack, minAttack):
        self.Name = Name
        self.HP = HP
        self.maxAttack = maxAttack
        self.minAttack = minAttack

    def getName(self):
        return self.Name

    def getMaxAttack(self):
        return self.maxAttack

    def getMinAttack(self):
        return self.minAttack

    def getHP(self):
        return self.HP


class Person(NPC):
    def __init__(self, Name="Person", maxHP=100, minHP=100, maxAttack=1, minAttack=1):
        self.HP = random.randint(minHP, maxHP)
        super(Person, self).__init__(Name, self.HP, maxAttack, minAttack)

class Zombie(NPC):
    def __init__ (self, Name="Zombie", maxHP=100, minHP=50, maxAttack=20, minAttack=10):
        self.HP = random.randint(minHP, maxHP)
        super(Zombie, self).__init__(Name, self.HP, maxAttack, minAttack)

class Vampire(NPC):
    def __init__ (self, Name="Vampire", maxHP=200, minHP=100, maxAttack=20, minAttack=10):
        self.HP = random.randint(minHP, maxHP)
        super(Vampire, self).__init__(Name, self.HP, maxAttack, minAttack)

class Ghoul(NPC):
    def __init__ (self, Name="Ghoul", maxHP = 80, minHP = 40, maxAttack = 30, minAttack = 15):
        self.HP = random.randint(minHP, maxHP)
        super(Ghoul, self).__init__(Name, self.HP, maxAttack, minAttack)


class Werewolf(NPC):
    def __init__ (self, Name="Werewolf", maxHP = 200, minHP = 200, maxAttack = 40, minAttack=0):
        self.HP = random.randint(minHP, maxHP)
        super(Werewolf, self).__init__(Name, self.HP, maxAttack, minAttack)

