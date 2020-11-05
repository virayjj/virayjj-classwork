class Dog:
    def __init__(self, name):
        self.name = name
        self.colour = ""
    #end function

    def set_colour(self, my_colour):
        if my_colour in ("Brown", "Black"):
            self.colour = my_colour
    #end function

    def get_colour(self):
        return self.colour
    #end function

    def get_name(self):
        return self.name
    #end function

class Puppy(Dog):
    def __init__ (self, name):
        super().__init__(name)
        self.shoesChewed = 0
    #end function

    def chewShoe(self, numShoes):
        self.shoesChewed = self.shoesChewed + numShoes
    #end function

    def getShoesChewed(self):
        return self.shoesChewed
    #endfunction

my_puppy = Puppy("Fido") # or any name

for x in range(0, 5): # or from 0 to any number
    my_puppy.chewShoe(1)
#next x

print(my_puppy.get_name())
print(my_puppy.getShoesChewed())
