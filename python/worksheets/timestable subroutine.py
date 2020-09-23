def multiples(table:int, startnum:int, endnum:int, pupilName:str):
    print("Hi, " + pupilName + " here is your times table: ")
    for value in range (startnum, endnum + 1):
        print(table, "x", value, "=", table*value)
    #next value
#end def

#main program
pupilName = str(input("Enter your name: "))
table = int(input("Enter a times table: "))
startnum = int(input("Enter a start number: "))
endnum = int(input("Enter an end number: "))
multiples(table, startnum, endnum, pupilName)
        
