#OOPS in python
#Classes contain attributes and behavior
#Class is a userdefined data type that we can create by ourselves

#Define class
class phone:                                #initial class definition
    def make_call(self,phone_number):
        print("Made a call to",phone_number)
    def play_game(self,name_of_game):
        print("Played the game",name_of_game)
    
samsung_A11 = phone()
samsung_A11.make_call("+919877675")
samsung_A11.play_game("Horizon Zero Dawn!")

#Define class with attributes and methods with params
class phone:                                #delayed class definition
    def set_color(self, color):
        self.color = color
    def set_cost(self,cost):
        self.cost = cost
    def show_color(self):
        return "color is " + self.color
    def show_cost(self):
        return "cost is "+ str(self.cost)   #typecast to str to add to string output
    
samsung_P11 = phone()
samsung_P11.set_color("blue")
samsung_P11.set_cost(12000)
print(samsung_P11.show_color())
print(samsung_P11.show_cost())

#Class with a constructor
class Employee:
    def __init__(self, name, age, salary, gender):
        self.name = name
        self.age = age
        self.salary = salary
        self.gender = gender

    def employee_details(self):
        print("Name:",self.name,", Age:",self.age,",Salary:",self.salary,",gender:",self.gender)

Simli = Employee("Simli",32,120000,"Female")
Simli.employee_details()
