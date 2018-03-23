from House import House
from Observer import Observable

class Neighborhood(Observable):
    def __init__(self, numHomes):
        super(Neighborhood, self).__init__()
        self.Houses = []
        for count in range(numHomes):
            newHouse = House(count)
            self.Houses.append(newHouse)
            self.add_Observer(newHouse)

        self.showNeighborhood()

    #Display houses with monster information
    def showNeighborhood(self):
        for count in range(len(self.Houses)):
            if ("SAFE" in self.Houses[count].Name):
                print (" __"+ self.Houses[count].Name + "___\n" +
                   " |                |\n" +
                   " |   " + str(len(self.Houses[count].Persons)) + " Persons    |\n"+ 
                   " |   " + str(len(self.Houses[count].Zombies)) + " Zombies    |\n"+
                   " |   " + str(len(self.Houses[count].Vampires)) + " Vampires   |\n"+
                   " |   " + str(len(self.Houses[count].Ghouls)) + " Ghouls     |\n"+
                   " |   " + str(len(self.Houses[count].Werewolves)) + " Werewolves |\n")
            else:
                print (" ______"+ self.Houses[count].Name + "_____\n" +
                   " |                |\n" +
                   " |   " + str(len(self.Houses[count].Persons)) + " Persons    |\n"+ 
                   " |   " + str(len(self.Houses[count].Zombies)) + " Zombies    |\n"+
                   " |   " + str(len(self.Houses[count].Vampires)) + " Vampires   |\n"+
                   " |   " + str(len(self.Houses[count].Ghouls)) + " Ghouls     |\n"+
                   " |   " + str(len(self.Houses[count].Werewolves)) + " Werewolves |\n")
     
    def getHouses (self):
        return self.Houses

