def calc(n):
    if n == 0:
        return 1 #we know 0! is 1 (base case/terminating condition)
    else:
        return n * calc(n-1)
    #end-if
#end-func

print(calc(0))
print(calc(5))
print(calc(10))
