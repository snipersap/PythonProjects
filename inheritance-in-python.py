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
class grand_parent:
    def __init__(self,era):                 #grand_parent constructor
        self.era = era                      #Unused attribute

    def set_name(self, name):
        self.name = name

    def set_age(self,age):
        self.age = age

    def show_name_age(self):                #original overridden method
        print("My name is:",self.name,"and I am",self.age,"years old!")

class parent(grand_parent):
    def __init__(self, era,country):        #parent constructor
        super().__init__(era)
        self.country = country

    def set_homes(self, homes):
        self.homes = homes
    
    def set_jobs(self, jobs):
        self.jobs = jobs
    
    def show_homes(self):
        print("I have",self.homes,"homes.")
    
    def show_jobs(self):
        print("I have",self.jobs,"jobs.")

class child(parent):
    def __init__(self, era, country,origin):            #child constructor
        super().__init__(era, country)
        self.origin = origin

    def set_cars(self, cars):
        self.cars = cars

    def set_boats(self,boats):
        self.boats = boats

    def show_cars(self):
        print("I have",self.cars,"cars.")

    def show_boats(self):
        print("I own",self.boats,"boats.")

    def show_name_age(self):                        #override grand_parent's method
        grand_parent.show_name_age(self)            #call grand_parent's method
        print("Overridden: I am",self.name,",",self.age,"years old, from",self.origin,"living in",self.country)

print("Multi-level Inheritance example >>")
Arnold = child("1940s","Tunisia","Maldives")
Arnold.set_name("Arnold Auddy")
Arnold.set_age(34)
Arnold.set_jobs(2)
Arnold.set_homes(4)
Arnold.set_cars(1)
Arnold.set_boats(1)

Arnold.show_name_age() #call overridden method
Arnold.show_boats()
Arnold.show_cars()
Arnold.show_homes()
Arnold.show_jobs()

##Hybrid Inheritance: When 2 or more inheritance types are used
class sibling(parent):              #Hybrid inheritance:has sibling(single), and grand parent(multi level)
    def __init__(self, era, country,sibling):
        super().__init__(era, country)
        self.sibling = sibling

    def show_sibling(self):
        print("My sibling is:",self.sibling)


Teesta = sibling("1950s","Jamaica",Arnold)
Teesta.show_sibling()