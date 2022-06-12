import ParentHuman
class ChildHuman(ParentHuman.ParentHuman1):
    #def greeting(self):
        #print("Hello!")
    def display(self):
        print("This is an overiden method")
child = ChildHuman("Jeff", "Wise", 6) 
child.display()
###
