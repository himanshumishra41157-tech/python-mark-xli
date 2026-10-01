import random

choice = ["snake" , "water" , "gun"]
computer = random.choice(choice)

try:
          user_input = input("enter snake , water , gun : ").lower()

          if user_input not in choice:
              raise ValueError("invalid input")


          if user_input not in choice:
             print("invalid input")
          else:
             print("valid input", computer)
          if user_input == computer:
             print("result is tie")
          elif user_input == "snake" and computer == "water":
             print("result is user wins")
          elif user_input == "water" and computer == "gun":
             print("result is user wins")
          elif user_input == "gun" and computer == "snake":
             print("result is user wins")

          else:
             print("result is computer wins")
except ValueError:
    print("invalid input")















    #this code is written by himanshu mishra the father of code