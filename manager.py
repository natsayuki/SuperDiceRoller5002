from classes.utils import Utils
from classes.utils import Fight
from classes.die import Die
from classes.player import Player

utils = Utils()

class Manager():
    D4 = Die(1, 4, "D4")
    D6 = Die(1, 6, "D6")
    D8 = Die(1, 8, "D8")
    D10 = Die(1, 10, "D10")
    D12 = Die(1, 12, "D12")
    D20 = Die(1, 20, "D20")
    WD4 = Die(3, 4, "Weighted D4")
    WD6 = Die(4, 6, "Weighted D6")
    WD8 = Die(5, 8, "Weighted D8")
    WD10 = Die(6, 10, "Weighted D10")
    WD12 = Die(7, 12, "Weighted D12")
    WD20 = Die(11, 20, "Weighted D20")
    possibleDice = [D4, D6, D8, D10, D12, D20, WD4, WD6, WD8, WD10, WD12, WD20]

    encounterMessages = ["You see a guy sitting around doing much.",
    "You stumble across a jerk. Mainly cause they tripped you.",
    "You approach a random person.", "That person looks like they want trouble.",
    "Someone is looking at you funny."]

    def welcome(self):
        print("Welcome to Super Dice Roller 5002!")
        name = utils.ask("What is your name?")
        print("Alright " + name + ". It is time for your dice rolling adventure to begin!")
        print("You can have this Weighted D6. It was my favourite die when I was your age.")
        print("Obtained Weighted D6!")
        print("Take good care of it.")
        return Player(name, [self.WD6], self.WD6)

    def main(self):
        player = self.welcome()
        running = True
        while running:
            enemy = utils.pick(self.possibleDice)
            message = utils.pick(self.encounterMessages)

            player.avoid = False

            player = utils.menu(enemy, player, message)

            fight = not player.avoid

            if fight:
                fightObj = Fight(player, enemy, self.possibleDice)
                fightRes = fightObj.main()

                if not isinstance(fightRes, bool):
                    player.dice.append(fightRes)
                else:
                    if fightRes:
                        player.streak += 1
                    else:
                        running = False
