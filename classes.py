class Person:
    #class attributes go before the __init__ function. Values of class attributes are constant between all instances of a class. 
    human_type = "homosapien" #variables not in the parameters are constants for all instances of Person class
    def __init__(self, name, age): #initializes values for each instance of the Person class

        self.name = name
        self.age = age 
    
    def description(self):
        print(f"{self.name} is {self.age} years old and is a {self.human_type}")
    
    def speak(self, word):
        print(f"{self.name} says {word}")

        
sharan = Person("Sharan", 17)

print(sharan.name)
print(sharan.age)
print(sharan.human_type)
sharan.description()
sharan.speak("Hello")

clay = Person("Clay", 18)
clay.description()

class Car:
    type = "Vehicle"
    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

    def getDescription(self):
        print(f"The {self.color} car has {self.miles} miles")


car1 = Car("White", 50000)
car1.getDescription()