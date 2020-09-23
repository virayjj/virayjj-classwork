password1 = 1
password2 = 2

def getPword(attempt):
    global password1
    global password2
    
    if attempt == 1:
        password1 = input("enter password: ")
        if len(password1) > 5 and len(password1) < 9 and not password1.isnumeric():
            password2 = input("enter password again: ")
        
        else:
            getPword(2)
        #end if
    elif attempt == 2:
        print("Error. password must be 6 to 8 characters long ")
        getPword(1)
    #end if
#end procedure

#main program
done = False
getPword(1)

while not done:
    if password1 == password2:
        print("password change successful")
        done = True
    else:
        print("error - passwords do not match")
        getPword(1)
    #end if
#end while
