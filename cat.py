# class are for 
#  bundling related data(like a dictionary)
#  with the functions that modify that data
#  Encapsulation - hiding the detail of how somthing is do inside a method
#  encapsulation,alternate defination
#  Inheritence - making specialized classes based on other classes
#  Polymorphism methods can interact with lots of diffrent kind of objects
#  and it doesn't care about class
#  Compostion not stuffing everything in to a single class.Instead make classes that help
#  other  classes.creat specialized classes that cooprated with each other

from random import randint
from toy import Toy
class Cat: 
    # __init__ python allows you to refer
    #  to an object as it's created
    # 
    def __init__(self,new_name,friendliness=0.5,happiness=10,cuddle_power =1):
        self.name = new_name
        self.friendliness= friendliness
        self.happiness = happiness
        self.cuddle_power = cuddle_power
    def recive_toy(self,toy):
        #  you can add new properties to an object in any method

        self.toy = toy 

    def play_with_toy(self):
        #  this increases the happiness
        print(f"{self.name} play with {self.toy.name}")
        self.happiness += self.toy.quality

    def greet(self,whom):
        print(f"Hello i am {self.name}.Nice to meet you {whom.name}!")

    def cuddle(self,whom):
        cuddle_chance = randint(0,10)/10
        if cuddle_chance >= self.friendliness:
            #  as long as "whom" has a .name and a . happiness
            #  the cuddle method can do its work
            # when the method interacts with diffrent kind of objects
            #  we call it polymorphism
            
            print(f"i cuddle you{whom.name}!")
            whom.happiness += self.cuddle_power
        else:
            print(f"Bad touch,bad touch!")
    
        

milla = Cat("Milla")
oakley = Cat("Oakley")# use the class  to creat
                #   instances is another word for objectt





