from classes.utils import Utils
class Player():
    def __init__(self, name, dice, equipped):
        self.name = name
        self.dice = dice
        self.equipped = equipped
        self.streak = 0
        self.avoid = False
    def switch(self):
        utils = Utils()
        dice = self.dice
        while 1:
            print("Your dice are:")
            for die in dice:
                print(die.name)
            answer = utils.ask("What do you want to equip?").lower()
            if answer in [die.name.lower() for die in dice]:
                new = [die for die in dice if die.name.lower() == answer][0]
                print("Equipped " + new.name + '!')
                return new
            else:
                print("You don't have that die.")
