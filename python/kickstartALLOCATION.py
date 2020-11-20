priceArray = []

def calc(casex, totalBudget):
    total = 0
    count = 0
    global priceArray
    priceArray.sort()
    for x in priceArray:
        total = total + x
        count = count + 1
        if total > totalBudget:
            count = count - 1
            break
    
    print("Case #",casex ,": ", count)
    priceArray.clear()
    
cases = int(input("Enter the number of cases: "))
for x in range(1,cases + 1):
    numHouses = int(input("Enter the number of houses: "))
    budget = int(input("Enter your budget: "))
    for y in range(1, numHouses + 1):
        housePrice = int(input("Enter price of house: "))
        priceArray.append(housePrice)  
    calc(x, budget)
    
