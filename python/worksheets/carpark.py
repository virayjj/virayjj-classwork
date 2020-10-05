### SRC - This is really great work, but I do want to see you
### use the coding conventions... End If etc.

carPark = [
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]
def parkACar():
    global carPark
    
    registration = input ("Enter your car registration: ")
    row = input ("Enter the park row: ")
    column = input ("Enter the park column: ")

    row = int(row) - 1
    column  = int(column) - 1
    
    if carPark[row][column] == 0:
        carPark[row][column] = registration
        displayCarParkGrid()
    else:
        parkACar()

def removeACar():
    global carPark

    registration = input ("Enter your car registration: ")
    row = input ("Enter the park row: ")
    column = input ("Enter the park column: ")

    row = int(row) - 1
    column  = int(column) - 1

    carPark[row][column] = 0

    displayCarParkGrid()
    
def displayCarParkGrid():
    global carPark
    for spaceRow in carPark:
        print(spaceRow)


