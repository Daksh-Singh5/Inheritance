#Write a program to create a base class Bird, with a constructor and two methods. Then, create a child class that inherits the constructor from Class Bird and has two functions. Finally, display how you can use Super to access the parent class constructor inside the child class.

class Bird:
    def __init__(self,Name,Type,flyORnot ):
        self.Name = Name
        self.Type = Type
        self.flyORnot = flyORnot
    
    def classprint(self):
        print("|",self.Name,"|",self.Type,"|",self.flyORnot,"|")

    def changename(changer,self):
        self.Name = changer

class hummingbird(Bird):
    def __init__(self, Name, Type, flyORnot,Where):
        self.Where = Where
        super().__init__(Name, Type, flyORnot)
    def classprint(self):
        print("|",self.Name,"|",self.Type,"|",self.flyORnot,"|")

    def changename(changer,self):
        self.Name = changer

Jerry =hummingbird("Jerry","Humming Bird","Can fly","In cities")

Jerry.classprint()
