class Dog():
    def __init__(self, dogName, myColour):
        self.__name = dogName
        self.__colour = myColour

    def bark(self, barkTimes):
        for n in range(barkTimes):
            print(self.__name + " says WOOF!")

    def setColour(self,myColour):
        self.__colour = myColour

    def getColour(self):
        return self.__colour

    def getName(self):
        return self.__name

    def printDogDetails(self):
        print(self.__name, self.__colour)

class Puppy(Dog):
# Puppy inherits attributes and methods from parent class Dog

# In Python, names starting with a double underscore are private
# They are not visible outisde the method
# This is data hiding, an important aspect of "encapsulation"

    def __init__(self, dogName, myColour, myDob):
        super().__init__(dogName, myColour) # Dog Constructor
        self.date = myDob
        self.shoesChewed = 0

    #public procedure chewShoe(myShoesChewed)
    def chewShoe(self, myShoesChewed):
        self.shoesChewed = self.shoesChewed + myShoesChewed
    #end procedure
        
    def getShoesChewed(self):
        return self.shoesChewed

    def bark(self, barkTimes): # overides the def bark in the Dog class
        super().bark(1) # but can also do the Dog class def bark
        for n in range (barkTimes):
            print("YAP!")

    def getDate(self):
        return self.date

myDog1 = Dog("Fido", "Black")
myDog2 = Dog("Boonie", "Golden")
myDog3 = Dog("Mutt", "Unknown")
myDog4 = Dog("Jeff", "Unknown")
puppy1 = Puppy("Malla", "Light Brown", "12/08/16")
puppy2 = Puppy("whatevah", "grey", "05/05/05")

myDog3.bark(3)
puppy1.bark(2)

puppy1.chewShoe(3)
puppy1.chewShoe(1)
print(puppy1.getName(), "has chewed", puppy1.getShoesChewed(), "shoes.")
print(puppy1.getName(), "has a date of birth of", puppy1.getDate())
