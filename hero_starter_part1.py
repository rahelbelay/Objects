


class Hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def attack(self, enemy):
        enemy.health -= self.power

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def print_status(self):
        print("%s has %d health and %s power ")%(self, self.health, self.power )




class Goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def attack(self,enemy):
        enemy.health -= self.power
    def print_status(self):
        print("%s has %d health and %s power ")%(self, self.health, self.power )


        
"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

def main():
    # hero_health = 10
    # hero_power = 5
    # goblin_health = 6
    # goblin_power = 2

    hero = Hero(40,50)
    goblin = Goblin(20,20)


    

    while goblin.health > 0 and hero.health > 0:
        print("You have %d health and %d power." % (hero.health, hero.power))
        print("The goblin has %d health and %d power." % (goblin.health, goblin.power))
        print()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            # Hero attacks goblin
        
            goblin.health -= hero.power
            print("You do %d damage to the goblin." % hero.power)
            if goblin.health <= 0:
                print("The goblin is dead.")
        elif user_input == "2":
            pass
        elif user_input == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            hero.health -= goblin.power
            print("The goblin does %d damage to you." % goblin.power)
            if hero.health <= 0:
                print("You are dead.")

main()