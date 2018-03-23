import random
from Observer import Observable
from Observer import Observer
from NPC import Werewolf
from NPC import Person
from NPC import Zombie
from NPC import Vampire
from NPC import Ghoul

class House(Observable, Observer):
    def __init__(self, count):
        super(House, self).__init__()
        self.Name = "House " + str(count)
        self.Persons =[]
        self.Zombies = []
        self.Vampires = []
        self.Ghouls = []
        self.Werewolves = []
        numMonsters = random.randint(1,10)
        for x in range(numMonsters):
            monsterType = random.randint(1,5)
            if (monsterType == 1):
                newMonster = Person()
                self.Persons.append(newMonster)
            elif (monsterType == 2):
                newMonster = Zombie()
                self.Zombies.append(newMonster)
            elif (monsterType == 3):
                newMonster = Vampire()
                self.Vampires.append(newMonster)
            elif (monsterType == 4):
                newMonster = Ghoul()
                self.Ghouls.append(newMonster)
            elif (monsterType == 5):
                newMonster = Werewolf()
                self.Werewolves.append(newMonster)

            if (newMonster.Name != "Person"):
                self.add_Observer(newMonster)
            if (len(self.observers) == 0):
                self.Name = self.Name + ": SAFE"
                
        self.update()

    def getObservers(self):
        return self.observers

    def getPersons(self):
        return self.Persons

    def getZombies(self):
        return self.Zombies

    def getVampires(self):
        return self.Vampires

    def getGhouls(self):
        return self.Ghouls

    def getWerewolves(self):
        return self.Werewolves

    #Print monsters in house with their HP
    def printInfo(self):
        for x in range(len(self.Zombies)):
            print ("Zombie " + str(x) + " HP:" + str(self.Zombies[x].HP))
        for x in range(len(self.Vampires)):
            print ("Vampire " + str(x) + " HP:" + str(self.Vampires[x].HP))
        for x in range(len(self.Ghouls)):
            print ("Ghoul " + str(x) + " HP:" + str(self.Ghouls[x].HP))
        for x in range(len(self.Werewolves)):
            print ("Werewolf " + str(x) + " HP:" + str(self.Werewolves[x].HP))
        print ("Persons: " + str(len(self.Persons)))

    #Choose a random creature in the house to attack the player
    def attackPerson(self, player):
        creatureType = random.randint(1,5)
        if (creatureType == 1):
            if (len(self.Persons) > 0):
                player.getAttacked(self.Persons[0])
            else: self.attackPerson(player)
        if (creatureType == 2):
            if (len(self.Zombies) > 0):
                player.getAttacked(self.Zombies[0])
            else: self.attackPerson(player)
        elif (creatureType == 3):
            if (len(self.Vampires) > 0):
                player.getAttacked(self.Vampires[0])
            else: self.attackPerson(player)
        elif (creatureType == 4):
            if (len(self.Ghouls) > 0):
                player.getAttacked(self.Ghouls[0])
            else: self.attackPerson(player)
        elif (creatureType == 5):
            if (len(self.Werewolves) > 0):
                player.getAttacked(self.Werewolves[0])
            else: self.attackPerson(player)
        
    #Get attacked by the player and whatever weapon was chosen
    def getAttacked(self, damage, weapon):
        for x in range(len(self.Zombies)):
            if (weapon.Name == "SourStraw"):
                self.Zombies[x].HP = self.Zombies[x].HP - (damage *2)
                print ("Zombie " + str(x) + " lost " + str(damage*2) + " HP (It's very effective!)")
            else:
                self.Zombies[x].HP = self.Zombies[x].HP - damage
                print ("Zombie " + str(x) + " lost "+ str(damage) + " HP")
            if (self.Zombies[x].HP < 0):
                print("Zombie " + str(x) + " is now a Person!")
            self.Zombies[x].update()
        for x in range(len(self.Vampires)):
            if (weapon.Name != "ChocolateBar"):
                self.Vampires[x].HP = self.Vampires[x].HP - damage
                print ("Vampire " + str(x) + " lost " + str(damage) + " HP")
            else: print("Vampire " + str(x) + " was unaffected")
            if (self.Vampires[x].HP < 0):
                print("Vampire " + str(x) + " is now a Person!")
            self.Vampires[x].update()
        for x in range(len(self.Ghouls)):
            if (weapon.Name == "ChocolateBar"):
                self.Ghouls[x].HP = self.Ghouls[x].HP - (damage*5)
                print ("Ghoul " + str(x) + " lost " + str(damage*5) + " HP (It's incredibly effective!)")
            else:
                self.Ghouls[x].HP = self.Ghouls[x].HP - damage
                print ("Ghoul " + str(x) + " lost " + str(damage) + " HP")
            if (self.Ghouls[x].HP < 0):
                print("Ghoul " + str(x) + " is now a Person!")
            self.Ghouls[x].update()
        for x in range(len(self.Werewolves)):
            if (weapon.Name == "HersheysKiss") or (weapon.Name == "NerdBomb"):
                self.Werewolves[x].HP = self.Werewolves[x].HP - damage
                print ("Werewolf " + str(x) + " lost " + str(damage) + " HP")
            else: print("Werewolf " + str(x) + " was unaffected")
            if (self.Werewolves[x].HP < 0):
                print("Werewolf " + str(x) + " is now a Person!")
            self.Werewolves[x].update()

        monstersDefeated = 0

        #Remove each monster that was turned back into a human from the monster and observer lists
        for x in reversed(self.Zombies):
            if (x.HP < 0):
                self.Zombies.remove(x)
                self.remove_Observer(x)
                monstersDefeated = monstersDefeated + 1
        for x in reversed(self.Vampires):
            if (x.HP < 0):
                self.Vampires.remove(x)
                self.remove_Observer(x)
                monstersDefeated = monstersDefeated + 1
        for x in reversed(self.Ghouls):
            if (x.HP < 0):
                self.Ghouls.remove(x)
                self.remove_Observer(x)
                monstersDefeated = monstersDefeated + 1
        for x in reversed(self.Werewolves):
            if (x.HP < 0):
                self.Werewolves.remove(x)
                self.remove_Observer(x)
                monstersDefeated = monstersDefeated + 1

        for x in range(monstersDefeated):
            newPerson = Person()
            self.Persons.append(newPerson)
            self.update()
        

        


