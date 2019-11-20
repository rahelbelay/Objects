# blueprint
#  a.k.a factory
#  a.k.a class

class Todo:
    #  instruction for how to constract
    #  a new Todo object
    # use the __init__() to creat instances
    #  of the Todo class
    #  This method is also known as the"constructor"
    #  "dunder"
    def __init__(self, title, completed = False):

    #  Assume that a new todo is not already completed
    #  so we set the default argument value to false
        self.title = title
        self.completed = completed


    # behaviors
    # Example of encapsulation ,hide the detals of how your code works

    def update_title(self, new_tilte):
        if self.title != new_tilte:
            self.updated_on = '2019-11-18'

    def update_completed(self,new_completed)
        self.completed = new_completed
            if self.completed:
                self.completed_on ='2019-11-18'
            





    def display(self):
        #  you must use self as a first argument 
        #  so that an object can call a function.
        #  it links the function to object
        print(self.title)
    def __str__(self):
        return f"{self.title}({self.completed})"