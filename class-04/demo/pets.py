# ABC class : In Python, an Abstract Base Class (ABC) is a special kind of class that cannot be instantiated directly. Instead, it is meant to be subclassed by other classes that will implement its abstract methods.

from abc import ABC, abstractmethod

class Pet: #super (parent) class

    count = 0

    def __init__(self ,name, age, breed) :
        self.name = name
        self.age = age
        self.breed = breed
        Pet.count+= 1
    
    def sleep(self):
        return f'is sleeping'
    
    @abstractmethod #decorater
    def speek(self):
        pass

    @classmethod
    def get_pets_count(cls):
        return cls.count
    

class Cat(Pet): #sub class (child)

    def __init__(self ,name, age, breed, color) :
        self.color = color
        super().__init__(name, age, breed)

    def __str__(self): # used to define the string representation of the obj to the end-users
        return f'My name is : {self.name} my age is {self.age} my breed is {self.breed}'
    
    def __repr__(self): # # used to define the string representation of the obj for the code it self
        return f'I am a representation of {self.name}'

    # override the speek method
    def speek(self):
        return f'{self.name} said miawww!'
    
    def purr(self):
        return "cat is purring!!!"
    
class Dog(Pet):

    def __init__(self ,name, age, breed) :
        super().__init__(name, age, breed)

    def speek(self):
        return f'{self.name} said wolfffff!'
    
    @staticmethod
    def get_avg_dogs_age():
        return 'The average age of dogs is 5 years!'
    
if __name__ == "__main__":
    sherry = Cat("sherry",1,"British","black")
    meshmesh = Cat("meshmesh",2,"American", "white")

    bobby = Dog("bobby", 3, "Amiarican")
    bobby2 = Dog("bobby", 3, "Amiarican")

    print(Pet.count)
    print(Pet.get_pets_count())

    # print(sherry.name)
    # print(sherry.color)
    # print(sherry.sleep())
    # print(sherry.speek())
    
    # print(bobby.name)
    # print(bobby.sleep())
    # print(bobby.speek())

    print(sherry)
    print(Dog.get_avg_dogs_age())

