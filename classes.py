class Person:
    #class attributes go before the __init__ function. Values of class attributes are constant between all instances of a class. 
    human_type = "homosapien" #variables not in the parameters are constants for all instances of Person class
    def __init__(self, name, age): #initializes values for each instance of the Person class

        self.name = name
        self.age = age 
    
    def description(self):
        print(f"{self.name} is {self.age} years old and is a {self.human_type}")

        
sharan = Person("Sharan", 17)

print(sharan.name)
print(sharan.age)
print(sharan.human_type)
sharan.description()

clay = Person("Clay", 18)
clay.description()