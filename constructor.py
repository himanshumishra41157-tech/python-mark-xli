# # # Constructor is a special method in a class that is automatically called when an object is created.
# #  It is mainly used to initialize the object's data members.

# class person:
#     def __init__(self , n , o):
#         print("Hey i am a person")
#         self.name = n
#         self.occupation = o              #consturctor hamesha none return krta hai


#     def info(self):
#         print(f"{self.name} is a {self.occupation}")


# a = person("Harry" , "AI devloper")
# b = person("Divya" , "Web devloper")
# # c =  person(1,2,3) ---->       TypeError: person.__init__() takes 3 positional arguments but 4 were given 
# #y ye error isliye dega q ki ye c ko ik argument ki tarah treat kr rha hai yani self= c
# c = o


# a.info()
# b.info()







# types of constructor
# 1. Default constructor --> A constructor that does not take any parameter other than self is called a default constructor.
# 2. parameterrized constructor --> Definition: A ed   constructor that accepts parameters to initialize the object's data is called a parameteriz




# Q.1🟢 Level 1 — Default Constructor

# Q1. Ek Student class banao jisme default constructor ho. Constructor automatically print kare:


class student:
    def __init__ (self):
        print("Hey i am a student")


s1 = student()




# 🔥 Real-life example: Bank Account

# Maan le bank me kisi customer ka account create kar rahe ho:

class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def info(self):
        print(self.name, "has ₹", self.balance)


a1 = BankAccount("Himanshu", 5000)
a2 = BankAccount("Rahul", 10000)

a1.info()
a2.info()