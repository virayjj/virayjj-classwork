total_student = 30

def classScore():
    global total_student
    count = 0
    score_total = 0
    
    while count < total_student:
        test_score = input("Enter students score: ")        
        score_total = score_total + int(test_score)
        count = count + 1

    return score_total


test1_average = classScore() / total_student
test2_average = classScore() / total_student
test3_average = classScore() / total_student

year_average = (test1_average + test2_average + test3_average) / 3

print("test1: ", test1_average)
print("test2: ", test2_average)
print("test3: ", test3_average)
print("year average: ", year_average)
        
        
