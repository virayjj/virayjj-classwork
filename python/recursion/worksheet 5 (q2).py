def sumNumbers(n):
    if n == 0:
        return n
    else:
        return n + sumNumbers (n -2)
    #end if
#end function 

sum = sumNumbers(10)
print ("sum = ", sum)

input("\nPress Enter to exit program. ")
