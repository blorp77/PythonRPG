from npc import NPC


class Combat:

    def __init__(self, hero, enemies):

        while True:
            if not hero.alive:
                print "You have fainted...\n"
                break
            self.turn(hero, enemies)
            remaining = False
            for enemy in enemies:
                remaining = remaining or enemy.alive
            if not remaining:
                print "You have won!\n"
                total_exp = 0
                for enemy in enemies:
                    total_exp += enemy.exp_given
                hero.gain_exp(total_exp)
                break
            for enemy in enemies:
                if enemy.alive:
                    hero.take_damage(enemy.deal_damage())

    def turn(self, hero, enemies):

        print "You are under attack by :"
        for num, enemy in enumerate(enemies):
            print "{}. Level {} {} : {}/{} HP".format(num+1, enemy.level, enemy.name, enemy.current_hp, enemy.total_hp)
        print "\nWhat do you do?"
        print "1. Attack"
        print "2. Flee"
        print "Your HP : {}/{}".format(hero.current_hp, hero.total_hp)
        while True:
            inp = raw_input("Choice (Enter = Attack) : ")
            if inp == '1' or inp == '':
                if len(enemies) > 1:
                    inp2 = raw_input("Which one? (Enter = first) ")
                    try:
                        if enemies[int(inp2)-1].alive:
                            self.attack(hero, enemies[int(inp2)-1])
                            break
                        print "You can't beat that bloody corpse!"
                        continue
                    except ValueError:
                        print "Bad choice! Attacking first by default."
                self.attack(hero, enemies[self.get_first_alive_enemy(enemies)])
                break
            elif inp == '2':
                print "You coward! Go back and fight!"
            else:
                print "Invalid command, try again."


    def attack(self, attacker, attacked):
        attacked.take_damage(attacker.deal_damage())

    def get_first_alive_enemy(self, enemies):
        for ind, enemy in enumerate(enemies):
            if enemy.alive:
                return ind