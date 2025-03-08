#Create a Bus child class inherited from the Vehicle class to calculate the total fare.

class vehicle:
    def __init__(self,Name,MaxSpeed,Mileage ):
        self.Name = Name
        self.MaxSpeed = MaxSpeed
        self.Mileage = Mileage

class bus(vehicle):
    def __init__(self, Name, MaxSpeed, Mileage,distance,fare):
        self.distance=distance
        self.fair = distance*10+fare
        super().__init__(Name, MaxSpeed, Mileage)

SchoolBus = bus("School Bus","50km/h","1 km per liter",20,0)

print(SchoolBus.Name,"|",SchoolBus.MaxSpeed,"|",SchoolBus.Mileage,"|",SchoolBus.fair)
        