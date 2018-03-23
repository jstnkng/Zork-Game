import random
from NPC import NPC
from Weapon import Weapon
from House import House
from Observer import Observer
from Neighborhood import Neighborhood
from Player import Player
from Game import Game

print (
       "It's a normal Halloween night, just like any other...\n" +
       "You have just finished a night of trick-or-treating, and you go to sleep.\n" +
       "However, when you wake up, you soon realize something isn't right...\n" +
       "Somehow your neighbors have been turned into ghastly creatures!!!\n" +
       "It is up to you to use your candy powers to turn them back to humans!\n\n" +
       "Some of your neighbors are still human and they can help give you health.\n\n" +
       "However, the rest have turned into:\n" +
       "Zombies: Attack Range: 0 - 10, Especially vulnerable to Sour Straws\n"+
       "Vampires: Attack Range: 10 - 20, Immune to Chocolate Bars\n" +
       "Ghouls: Attack Range: 15-30, Especially vulnerable to Nerd Bombs\n" +
       "Werewolves: Attack Range: 0-40, Immune to Chocolate Bars and Sour Straws\n\n"
      "There are anywhere between 1-10 of these creatures in each house around you.\n"
       )
def  getAnswer():
        answer = input('Are you brave enough to face this challenge??  ')
        if ("Yes" in answer):
            print("Good! The neighborhood needs you!\nLet's get started\n\n")
            zork = Game()
        elif ("No" in answer):
            print ("I don't blame you...but you should be ashamed.")
            exit()
        else:
            print ("Sorry, I can't understand you... (try typing Yes or No)")
            self.getAnswer()

            
getAnswer()

