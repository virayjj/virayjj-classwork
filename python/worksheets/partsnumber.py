part_number = 0
amount = 0
old_amount = 0

while int(part_number) != 9999:
    part_number = input("enter the part number: ")
    
    if len(part_number) == 4:
        amount = amount + 1
        
        if part_number[-1] == "6" or part_number[-1] == "7" or part_number[-1] == "8":
            old_amount = old_amount + 1
    else:
        print("invalid input")
        
print("Total number of parts: ", amount - 1)
print("Total number of odd parts: ", old_amount)
