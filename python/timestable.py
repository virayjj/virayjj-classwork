valid = False
times_table = 0

while not valid:
    num1 = input ("Enter a number for your timestable, from 1 to 20: ")
    if num1.isnumeric():
        num1 = int(num1)
        if num1 > 0 and num1 < 21:    
            columns = input("How many columns do you want: ")
            if columns.isnumeric():
                columns = int(columns)
                for x in range (1, columns + 1):
                    print(num1*x)
                    valid = True
            else:
                print ("The input must be a number")
            # --  end if
        else:
            print ("The input must be a number")
        # -- end if
    else:
        print ("The input must be a number")
    # -- end if
# -- end while
