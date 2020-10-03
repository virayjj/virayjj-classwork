import time

def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)
    #end if
#end function
    
def fib2(n):
    fibNumbers = [1,1] #list of first two Fibonacci numbers
    #now append the sum of the two previous numbers to the list
    for i in range(2, n):
        fibNumbers.append(fibNumbers[i-1] + fibNumbers[i-2])
    #next i
    return fibNumbers
#end function

num = input("Enter a number from 3 to 30: ")
num = int(num)

startTime1 = time.perf_counter()
print(fib(num))
endTime1 = time.perf_counter()
print("Time 1: {} seconds".format(endTime1 - startTime1))

startTime2 = time.perf_counter()
print(fib2(num))
endTime2 = time.perf_counter()
print("Time 2: {} seconds".format(endTime2 - startTime2))
