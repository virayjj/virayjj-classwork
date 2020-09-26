import random
done = False
while not done:
     choice = input("Enter your choice 1[rock], 2[paper] or 3[scissors]: ") 
     if int(choice) > 0 and int(choice) < 4:
          computer = random.randint(1,3)
          #print(choice, computer)
          if (int(choice) == 1 and computer == 2) or (int(choice) == 2 and computer == 3) or (int(choice) == 3 and computer == 1): print("player lost")
          elif int(choice) == computer: print("tie")
          else: print("player won")
          #end if
          end = input("play again? Y/N ")
          if end == "n" or end == "N": done = True 
          #end if
     #end if
#end while
