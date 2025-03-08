class vehical:
    def __init__(self,Name,MaxSpeed,Mileage ):
        self.Name = Name
        self.MaxSpeed = MaxSpeed
        self.Mileage = Mileage

class bus(vehical):
    pass

SchoolBus = bus("School Bus","50km/h","1 km per liter")

print(SchoolBus.Name,"is the name\n",SchoolBus.MaxSpeed,"is the Max Speed\n",SchoolBus.Mileage,"is the mileage\n")
        