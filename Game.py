from Player import Player
from Neighborhood import Neighborhood
import sys

class Game:
    def __init__(self):
        self.Player = Player()
        numHomes = 0
        while (numHomes < 1):
            try:
                numHomes = int(input('How many homes would you like to attempt to save? '))
            except:
                print ("Enter a valid integer")
            
        self.Neighborhood = Neighborhood(numHomes)
        self.beginGame()

    def getPlayer(self):
        return self.Player

    def getNeighborhood(self):
        return self.Neighborhood

    #Begin playing the game, loop until either we reach an end condition
    def beginGame(self):
        #If all the monsters in each house are killed
        while (len(self.Neighborhood.observers) > 0):
            while (True):
                currentHouse = 0
                try:
                    currentHouse = int(input("Which house would you like to attack? "))
                    if (currentHouse > len(self.Neighborhood.Houses)):
                        raise ValueError()
                except:
                    print ("Enter a valid house number")
                        
                homes = self.Neighborhood.getHouses()
                if ("SAFE" in homes[currentHouse].Name):
                    print ("This house is already safe.")
                else: break

            #If all the monsters in the current house are killed
            while (len(homes[currentHouse].getObservers()) > 0):
                self.Player.attackHouse(homes[currentHouse])
                print("====================================================\n")
                homes[currentHouse].attackPerson(self.Player)
                print("====================================================\n")
                weapons = len(self.Player.getKisses()) + len(self.Player.getStraws()) + len(self.Player.getChocolates()) + len(self.Player.getNerds())
                
                if (self.Player.getHP() < 1):
                    print ("You were killed by the creatures\n" +
                           "GAME OVER")
                    sys.exit()
                elif (weapons < 1):
                    print ("You are all out of weapons!\n")
                    print ("GAME OVER")
                    sys.exit()
                
                 

            self.Neighborhood.Houses[currentHouse].Name = self.Neighborhood.Houses[currentHouse].Name + ": SAFE"
            self.Neighborhood.remove_Observer(homes[currentHouse])
            self.Neighborhood.showNeighborhood()

        print("====================================================\n")
        print ("Congratulations! You have turned all the monsters back into persons and saved the neighborhood!")
        sys.exit()


