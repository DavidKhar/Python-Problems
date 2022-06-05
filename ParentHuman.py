# inheritence:
# create a class (blueprint/concept, like 'human', has methods, functions), and create an object of that class,
# you create attributes like 'name', 'height', etc.
# you can create a child class that gets a few of the things from it's parents. you can make it 'inherit' its parent class.
# inheritence makes thing neater and more readable



# UPDATE NISHIT ON HOMEWORK STATUS BY SATURDAY MORNING
# basic parent human class
class ParentHuman1:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def display(self, name):
        print(name)

parent = ParentHuman1("John", "Doe", 53) 
parent.display("david")