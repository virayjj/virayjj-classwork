nameList = ["", "", "", "", "", "", "", "", "", ""]

def displayMenu():
    print("1. Add name")
    print("2. Display list")
    print("3. Quit")
    print("")

    valid = False
    while not valid:
        choice = input("Enter your choice: ")
        choice = int(choice)
        
        if choice >= 1 and choice <= 3:
            valid = True
            if choice == 1:
                addName()
            elif choice == 2:
                showList()
            else:
                print("Program terminating")
        else:
            print("Invalid choice - please re-enter: ")

        
def addName():
    global nameList
    
    name = input("Enter the name to be added to the list: ")
    pos = input("Enter te position in the list to insert the name (1-10)")
    pos = int(pos)

    if name != "" and not name.isnumeric() and pos > 0 and pos < 11:
        nameList[pos - 1] = name
        displayMenu()
    else:
        print("Position must be from 1 to 10")
        addName()
    
def showList():
    global nameList
    pos = 0
    
    for name in nameList:
        pos = pos + 1
        print(pos, name)

    print("")
    displayMenu()


displayMenu()


