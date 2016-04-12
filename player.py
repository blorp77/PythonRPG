from npc import NPC


class Player(NPC):

    def __init__(self, name, level, hp, min_dmg, max_dmg, armor, light=0):
        NPC.__init__(self, name, level, hp, min_dmg, max_dmg, armor)
        self.exp = 0
        self.light = light

    def level_up(self):
        print "\n**LEVEL UP**"
        self.level += 1
        self.total_hp += self.level * 2
        self.current_hp = self.total_hp
        self.min_dmg += 1
        self.max_dmg += 1
        #self.armor += 1
        raw_input("*PRESS ENTER TO CONTINUE*")

    def gain_exp(self, exp):
        print "You have gained {} experience points.".format(exp)
        self.exp += exp
        needed_to_level = (self.level ** 2) * 50
        if self.exp >= needed_to_level:
            self.level_up()

    def display_status(self):
        print "\n********** Status **********"
        print "Name :", self.name
        print "Level :", self.level
        print "Experience : {} ({} before you level up)".format(self.exp, ((self.level ** 2) * 50) - self.exp)
        print "Hit points : {}/{}".format(self.current_hp, self.total_hp)
        print "Damage : {}-{}".format(self.min_dmg, self.max_dmg)
        print "Armor :", self.armor
        print "Light radius bonus :", self.light
        print "****************************\n"
        raw_input("*PRESS ENTER TO CONTINUE*")