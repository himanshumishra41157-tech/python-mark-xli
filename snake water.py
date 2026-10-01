# import random

# choice = ["snake" , "water" , "gun"]
# computer = random.choice(choice)

# try:
#           user_input = input("enter snake , water , gun : ").lower()

#           if user_input not in choice:
#               raise ValueError("invalid input")
#           else:
#              print("valid input", computer)
#           if user_input == computer:
#              print("result is tie")
#           elif user_input == "snake" and computer == "water":
#              print("result is user wins")
#           elif user_input == "water" and computer == "gun":
#              print("result is user wins")
#           elif user_input == "gun" and computer == "snake":
#              print("result is user wins")

#           else:
#              print("result is computer wins")
# except ValueError as error:
#     print(error)















#     #this code is written by himanshu mishra the father of code






import random

choice = ["snake", "water", "gun"]
computer = random.choice(choice)

try:
    user_input = input("Enter snake, water, or gun: ").lower()

    if user_input not in choice:
        raise ValueError(
            "Invalid choice! Please enter snake, water, or gun."
        )

    print("Valid input")
    print("Computer chose:", computer)

    if user_input == computer:
        print("Result is tie")
    elif user_input == "snake" and computer == "water":
        print("Result is user wins")
    elif user_input == "water" and computer == "gun":
        print("Result is user wins")
    elif user_input == "gun" and computer == "snake":
        print("Result is user wins")
    else:
        print("Result is computer wins")

except ValueError as error:
    print("Error:", error)

# This code is written by Himanshu Mishra, the father of code