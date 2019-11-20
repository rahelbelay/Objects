from cat import Cat 

# "Give me everything in Cat so i can customize my version"
# we say this inheritence
# CuddlyCat a sub class of Cat
# Cat is supperclass of CuddlyCat 
class CuddlyCat(Cat):
    def __init__(self,new_name):
        super().__init__(new_name, 0.9, 50, 5)
        print("the cuddly cat sleep.")



    def cuddles(self,whom):
        cuddle_chance = randint(0,10)/10
        if cuddle_chance <= self.friendliness:
            print(f"i cuddle you, {whom,name}!")
            whom.happines *= self.cuddle_power
        else:
            print(f"Bad touch, bad touch!")
artemis = CuddlyCat("Artie")
