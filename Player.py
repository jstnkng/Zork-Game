import random
from Weapon import HersheysKiss
from Weapon import SourStraw
from Weapon import ChocolateBar
from Weapon import NerdBomb

class Player:
    def __init__(self):
        self.HP = random.randint(100,125)
        self.Attack = random.randint(10,20)
        self.Kisses = []
        self.Straws = []
        self.Chocolates = []
        self.Nerds = []
        print ("Your starting HP is " + str(self.HP))
        print ("Your attack is " + str(self.Attack))
        for count in range(10):
            weaponType = random.randint(1,4)
            if (weaponType == 1):
                newWeapon = HersheysKiss()
                self.Kisses.append(newWeapon)
            elif (weaponType == 2):
                newWeapon = SourStraw()
                self.Straws.append(newWeapon)
            elif (weaponType == 3):
                newWeapon = ChocolateBar()
                self.Chocolates.append(newWeapon)
            elif (weaponType == 4):
                newWeapon = NerdBomb()
                self.Nerds.append(newWeapon)
                
        print ("\nOn Halloween, you picked: \n"
           + str(len(self.Kisses)) + " Hershey's Kisses\n" +
           " - Attack Modifier: 1\n" +
           " - Each can be used an unlimited amount of times\n"
           + str(len(self.Straws)) + " Sour Straws\n" +
           " - Attack Modifier: 1-1.75 \n" +
           " - Each can be used twice\n"
           + str(len(self.Chocolates)) + " Chocolate Bars\n" +
           " - Attack Modifier: 2-2.4\n" +
           " - Each can be used four times\n"
           + str(len(self.Nerds)) + " Nerd Bombs\n" +
           " - Attack modifier: 3.5-5\n" +
           " - Each can be used once\n" )

    def getHP(self):
        return self.HP

    def setHP(newHP):
        self.HP = newHP

    def getAttack(self):
        return self.Attack

    def getKisses(self):
        return self.Kisses

    def getStraws(self):
        return self.Straws

    def getChocolates(self):
        return self.Chocolates

    def getNerds(self):
        return self.Nerds

    #Get attacked by a random monster in the house the player is in
    def getAttacked(self, monster):
        minAttack = int(monster.getMinAttack())
        maxAttack = int(monster.getMaxAttack())
        attack = random.randint(minAttack, maxAttack)
        if (monster.getName() == "Person"):
            self.HP = self.HP + 1
            weaponType = random.randint(1,4)
            weaponType = random.randint(1,4)
            if (weaponType == 1):
                newWeapon = HersheysKiss()
                self.Kisses.append(newWeapon)
            elif (weaponType == 2):
                newWeapon = SourStraw()
                self.Straws.append(newWeapon)
            elif (weaponType == 3):
                newWeapon = ChocolateBar()
                self.Chocolates.append(newWeapon)
            elif (weaponType == 4):
                newWeapon = NerdBomb()
                self.Nerds.append(newWeapon)

            print("A Person in the house helped you! Your HP is now " +str(self.HP))
            print("You have also been given a " + newWeapon.Name)
        else:
            self.HP = self.HP - attack
            print ("A " + monster.Name + " attacked you for: " + str(attack))
            print ("Your HP is now " + str(self.HP))

    #Display weapons remaining and allow player to pick one to use
    def selectWeapon(self):
        kissesLeft = 0
        if (len(self.Kisses) > 0):
            kissesLeft = 1
            
        strawsLeft = 0
        for x in range(len(self.Straws)):
            strawsLeft = strawsLeft + self.Straws[x].getUses()

        chocolatesLeft = 0
        for x in range(len(self.Chocolates)):
            chocolatesLeft = chocolatesLeft + self.Chocolates[x].getUses()

        nerdsLeft = 0
        for x in range(len(self.Nerds)):
            nerdsLeft = nerdsLeft+ self.Nerds[x].getUses()
        
        while (True):
            kisses = "0"
            if (kissesLeft > 0):
                kisses = "Infinite"
            choice = input(("Choose a weapon: \n" +
                   " 1 = Hershey Kiss: " + kisses + " uses remaining\n" +
                   " 2 = Sour Straw: " + str(strawsLeft) + " uses remaining\n" +
                   " 3 = Chocolate Bar: " + str(chocolatesLeft) + " uses remaining\n" +
                   " 4 = Nerd Bomb: " + str(nerdsLeft) + " uses remaining\n"))

            try:
                choice = int(choice)
            except:
                continue
                
            
            if (choice == 1):
                weapon = HersheysKiss()
                break
            elif (choice == 2):
                if (len(self.Straws) > 0):
                    weapon = self.Straws[0]
                    weapon.useWeapon()
                    if (weapon.getUses() == 0):
                        self.Straws.remove(weapon)
                    break
                else:
                    print("Looks like you're out of this weapon. Select a different one")
                    continue
            elif (choice == 3):
                if (len(self.Chocolates) > 0):
                    weapon = self.Chocolates[0]
                    weapon.useWeapon()
                    if (weapon.getUses() == 0):
                        self.Chocolates.remove(weapon)
                    break
                else:
                    print("Looks like you're out of this weapon. Select a different one")
                    continue
            elif (choice == 4):
                if (len(self.Nerds) > 0):
                    weapon = self.Nerds[0]
                    weapon.useWeapon()
                    if (weapon.getUses() == 0):
                        self.Nerds.remove(weapon)
                    break
                else:
                    print("Looks like you're out of this weapon. Select a different one")
                    continue

        return weapon

    #Attack the house the player is currently in with the selected weapon
    def attackHouse (self,house):
        house.printInfo()
        weapon = self.selectWeapon()

        minDamage = int(weapon.getMinDamage())
        maxDamage = int(weapon.getMaxDamage())

        modifier = random.randint(minDamage, maxDamage)/100
        
        damage = self.Attack * modifier
        print ("====================================================\n")
        print("Your attack " + str(self.Attack) + " * weapon modifier of " + str(modifier) + " =  Total attack of: " + str(int(damage)))
        house.getAttacked(int(damage), weapon)
