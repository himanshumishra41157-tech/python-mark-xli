import random

choice = ["snake" , "water" , "gun"].lower()
computer = random.choice(choice)

user_input = input("enter snake , water , gun : ")

if user_input == computer:
    print("draw")
elif user_input == "snake" and computer == "water":
    print("user wins")
elif user_input == "water" and computer == "gun":
    print("user wins")
elif user_input == "gun" and computer == "snake":
    print("user wins")

else:
    print("computer wins")