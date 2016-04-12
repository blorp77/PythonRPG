import random
import math


class NPC:
    """
    name = ""
    level = 1
    current_hp = 0
    total_hp = 0
    min_dmg = 0
    max_dmg = 0
    armor = 0
    alive = True
    """
    def __init__(self, name, level, hp, min_dmg, max_dmg, armor, exp_given=0):
        self.name = name
        self.level = level
        self.current_hp = hp
        self.total_hp = hp
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg
        self.armor = armor
        self.alive = True
        self.exp_given = exp_given

    def heal(self, amount):
        self.current_hp += amount
        if self.current_hp > self.total_hp:
            self.current_hp = self.total_hp

    def take_damage(self, amount, include_armor=True):
        if include_armor:
            amount -= self.armor
        if amount > 0:
            self.current_hp -= amount
            print "{} takes {} damage.".format(self.name, amount)
            if self.current_hp <= 0:
                self.alive = False
                self.current_hp = 0
                print "**{} has died.".format(self.name)
        else:
            print "{} takes no damage.".format(self.name)


    def deal_damage(self):
        return int(math.floor((self.max_dmg + 1 - self.min_dmg) * random.random()) + self.min_dmg)
