from npc import NPC
from combat import Combat
from player import Player

import random
import math

map_file = "map.txt"

class RPG():

    def __init__(self):
        #Initial setup
        print "** Welcome to BoredRPG **\n"
        self.game_map = self.get_map()
        self.i, self.j = self.get_initial_position_of_player()
        name = raw_input("What ist thine name, brave warrior? ")
        self.hero = Player(name, 1, 20, 4, 6, 1, 0)
        self.encounter_odd = 0.0
        while True:
            if self.hero.alive:
                print "What do you do?"
                print "1. Move."
                print "2. Look around you."
                print "3. Rest for a bit."
                print "4. Display your status."
                print "5. Quit. I'm not bored anymore."
                inp = raw_input("Choice : ")
                if inp == '1':

                    while True:
                        print "\n**Where do you want to move? (N, W, S, E) (Enter to go back to main menu)"
                        self.draw_map(1)
                        inp2 = raw_input("Direction : ")
                        if inp2 == 'n' or inp2 == 'N':
                            self.move_to(self.i-1, self.j)
                        elif inp2 == 'w' or inp2 == 'W':
                            self.move_to(self.i, self.j-1)
                        elif inp2 == 's' or inp2 == 'S':
                            self.move_to(self.i+1, self.j)
                        elif inp2 == 'e' or inp2 == 'E':
                            self.move_to(self.i, self.j+1)
                        else:
                            break
                elif inp == '2':
                    self.look_around()
                elif inp == '3':
                    print "Resting"
                elif inp == '4':
                    self.hero.display_status()
                elif inp == '5':
                    print "Quitting"
                    exit(0)
                else:
                    print "Invalid command, try again."
            else:
                print "***GAME OVER YEAAAAAAAAAH***"
                exit()

    def get_map(self):
        f = open("map.txt", "r")
        new_map = []
        for line in f:
            new_map.append(list(line.rstrip("\n")))
        return new_map

    def get_initial_position_of_player(self):
        for i, row in enumerate(self.game_map):
            for j, col in enumerate(row):
                if col == 'S':
                    return i, j
        print "Map is invalid. There is no start point."
        exit(0)

    def look_around(self):
        print "You take some time to explore your surroundings..."
        self.draw_map(2)
        print "Legend : @ = YOU!, # = wall, ~ = water (outside of map), S = Start, E = Exit!, T = Treasure!!"


    def draw_map(self, radius=1):
        radius += self.hero.light
        map_string = "*~" + "~" * (radius - 1) + "Map" + "~" * (radius - 1) + "~*\n"
        for i in range(-radius, radius+1):
            map_string += "| "
            for j in range(-radius, radius+1):
                if i == 0 and j == 0:
                    map_string += '@' #This is you
                else:
                    map_string += self.get_char_from_map_at_pos(self.i+i, self.j+j)
            map_string += " |\n"
        map_string += "*~" + "~" * (radius*2 + 1) + "~*"
        print map_string

    def get_char_from_map_at_pos(self, i, j):
        try:
            return self.game_map[i][j]
        except IndexError:
            return "~"

    def move_to(self, i, j):
        move = self.game_map[i][j]
        if move == '#':
            print "You run into a wall and take 1 damage."
            self.hero.take_damage(1, False)
        else:
            self.i = i
            self.j = j
            self.encounter_odd += 0.05
            if move == 'E':
                print "Congratulations! You've reached the end of this floor!"
                exit(0)
            elif move == 'T':
                self.find_treasure()
                self.game_map[i][j] = ' ' #Removes the treasure chest from the game
            elif move == "S":
                print "Back to start! What now?"
            else:
                #Move into corridor, generate random fight here.
                dice_roll = random.random()
                if dice_roll < self.encounter_odd:
                    #BATTLE!
                    Combat(self.hero, [NPC("Goblin", 1, 10, 1, 2, 0, 20)])
                    self.encounter_odd = 0.0
                elif dice_roll > 0.95:
                    print "Surprise! You found something."
                else:
                    #Move normally
                    print "All is good, keep going!"
                    pass
        """
        Combat(hero, [NPC("Goblin", 1, 10, 1, 2, 0, 20),
                      NPC("Hobgoblin", 2, 20, 2, 4, 0, 30),
                      NPC("Goblin", 1, 10, 1, 2, 0, 20)
                      ])
        """

    def find_treasure(self):
        print "You found a treasure! Let's see what's inside..."
        dice_roll = random.random()
        if dice_roll < 0.40:
            hp_gain = (random.random() * (self.hero.level * 2)) + 1
            self.hero.total_hp += hp_gain
            self.hero.current_hp += hp_gain
            print "Found a health tonic! You gain {} hit points!".format(hp_gain)
        elif dice_roll < 0.70:
            pass

if __name__ == "__main__":
    RPG()