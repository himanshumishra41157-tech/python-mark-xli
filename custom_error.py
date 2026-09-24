# salary = int(input("enter your present salary: "))
# if salary < 1000 :
#     print("your salary is less than 1000")
# else:
#     raise ValueError("your salary is not valid")


# salary = input("enter your present salary: ")
# if salary == "quit":
#     print("okay quit bro")
# else:
#     raise ValueError("your salary is not valid")

# #Q.)User se age lo. Agar age negative ho to ValueError raise karo: "Age cannot be negative

# age = int(input("enter your age: "))
# if age >= 0:
#     print("your age is valid")
# else:
#     raise ValueError("age cannot be negative")

# q.) User se marks lo. Agar marks 0 se kam ya 100 se zyada ho to ValueError raise karo.

# marks = int(input("enter your marks: "))
# if marks < 100:
#     print("your marks is valid")
# elif marks > 100:
#     raise ValueError("your marks is not valid")


# Q.)) Do numbers lo aur divide karo. Agar second number 0 ho to ZeroDivisionError raise karo:
# "Cannot divide by zero"

# first_num = int(input("enter first number:"))
# sec_num = int(input("enter the second num:"))

# if sec_num == 0:
#     raise ZeroDivisionError("cannot divide by zero")
# else:

#     function = first_num / sec_num
#     print(function)


#Q.) User se password lo. Agar password ki length 8 se kam ho to ValueError raise karo.

paasword = input("enter your paasword:")
if len(paasword) < 8:
    raise ValueError("your paasword is not valid")
else:
    print("your paasword is valid beta ")
