from classes.die import Die
from random import randint
class Utils():
    def ask(self, question):
        return input(question + ': ')
    def pick(self, list):
        return list[randint(0, len(list) -1)]
    def menu(self, enemy, player, message):
        player.avoid = False
        while 1:
            print(message + " It looks they have a " + enemy.viewName)
            answer = self.ask("What action will you take?").lower()
            if answer in ['s', 'switch']:
                player.equipped = player.switch()
            elif answer in ['a', 'avoid']:
                if randint(0, 2) != 0:
                    player.avoid = True
                    print("Your evassive maneuver paid off.")
                    return player
                else:
                    print("Your pitiful attempt at escape fell through.")
                    return player
            elif answer in ['f', 'fight']:
                return player
            elif answer in ['?']:
                print("Type:")
                print("(S)witch to switch dice.")
                print("(A)void to attempt to avoid the encounter.")
                print("(F)ight to jump right in to the action.")
class Fight():
    def __init__(self, player, enemy, possibleDice):
        self.player = player
        self.enemy = enemy
        self.possibleDice = possibleDice
        self.utils = Utils()
    def main(self):
        while 1:
            print("You both roll your dice!")
            yourRoll = self.player.equipped.roll()
            enemyRoll = self.enemy.roll()
            if yourRoll == enemyRoll:
                self.tie(yourRoll)
            elif enemyRoll > yourRoll:
                return self.lose(yourRoll, enemyRoll)
            elif yourRoll > enemyRoll:
                return self.win(yourRoll, enemyRoll)
    def win(self, yourRoll, enemyRoll):
        print("You see the enemy's " + str(enemyRoll) + " and raise them a " + str(yourRoll) + '.')
        print("That's a victory for you!")
        if randint(0, 1) == 1:
            newDice = self.utils.pick(self.possibleDice)
            print("Wow! Your oponent was nice and gave you a shiny new " + newDice.name + " for winning!")
            self.utils.ask("Press enter to continue...")
            return newDice
        self.utils.ask("Press enter to continue...")
        return True
    def lose(self, yourRoll, enemyRoll):
        print("The enemy rolled a " + str(enemyRoll) + " to your " + str(yourRoll) + ".")
        print("Unfortunate. Your run is over.")
        print("You had a streak of " + str(self.player.streak))
        self.utils.ask("Press enter to continue...")
        return False
    def tie(self, yourRoll):
        print("By Jove! You have both rolled " + str(yourRoll) + "!")
        print("This calls for a re-roll!")
        self.utils.ask("Press eneter to continue...")
