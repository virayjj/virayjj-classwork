RED = (255,0,0)
BLACK = (0,0,0)
BLUE = (50,50,255)
YELLOW = (255,255,0)

class Shape():
    def __init__(self, myColourFill, myColourOutline):
        self.colourFill = myColourFill
        self.colourOutline = myColourOutline
        self.area = 0

    def calculateArea(self, mySide):
        self.area = mySide * mySide

class Rectangle(Shape):
    def __init__(self, myColourFill, myColourOutline, myHeight, myWidth):
        super().__init__(myColourFill, myColourOutline)
        self.height = myHeight
        self.width = myWidth

    def calculateArea(self):
        return (self.height * self.width)

class Circle(Shape):
    def __init__(self, myColourFill, myColourOutline, myRadius):
        super().__init__(myColourFill, myColourOutline)
        self.radius = myRadius

    def calculateArea(self):
        return (3.14 * (self.radius * self.radius))
    

myRec = Rectangle(RED, BLACK, 4, 6)
myCirc = Circle(YELLOW, BLUE, 3)
print(myRec.calculateArea())
print(myCirc.calculateArea())
