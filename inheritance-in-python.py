#Different types of inheritance
# Single 
# Multiple
# Multi-level
# Hybrid

##Single Inheritance: child dervied from one parent
class vehicle:
    def __init__(self,medium,tyres,length):
        self.medium = medium
        self.tyres = tyres
        self.length = length

    def show_vehicle_details(self):
        print("Medium:",self.medium,",tyres:",self.tyres,",length:",self.length)

class car(vehicle):
    def __init__(self, medium, tyres, length, brand, driving_side):
        super().__init__(medium,tyres,length)
        self.brand = brand
        self.driving_side = driving_side
    
    def show_car_details(self):
        print("Brand:",self.brand,",driving_side:",self.driving_side)

print("Single Inheritance example:")
Skoda_V1 = car("Road",4,"3m","Skoda","right")
print("Car is derived from Vehicle.")
Skoda_V1.show_vehicle_details()
Skoda_V1.show_car_details()

##Multiple inheritance: child derived from multiple parents
class cars:
    def __init__(self, brand, wheels):
        self.wheels = wheels
        self.brand = brand
    
    def show_car_details(self):
        print("Brand:",self.brand,",Wheels:",self.wheels)

class boat:
    def __init__(self,speed, length):
        self.speed = speed
        self.length = length

    def show_boat_details(self):
        print("Speed:",self.speed,"Length:",self.length)

class hydrocar(cars,boat):
    def __init__(self, brand, wheels, speed, length,type):
        cars.__init__(self, brand, wheels)      #separate parent class __init__ methods
        boat.__init__(self, speed, length)
        self.type = type

    def show_hydrocar_details(self):
        print("Type:", self.type)

print("Multiple Inheritance example:")
Honda = hydrocar("Honda",5,"20 Knots","4m","speedster")
Honda.show_car_details()
Honda.show_boat_details()
Honda.show_hydrocar_details()


##Multi-level inheritance: child derived from grandparent
#TODO>>