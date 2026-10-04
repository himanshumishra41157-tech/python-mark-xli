# # Constructor is a special method in a class that is automatically called when an object is created.
#  It is mainly used to initialize the object's data members.

class person:
    def __init__(self , n , o):
        print("Hey i am a person")
        self.name = n
        self.occupation = o              #consturctor hamesha none return krta hai


    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person("Harry" , "AI devloper")
b = person("Divya" , "Web devloper")
# c =  person(1,2,3) ---->       TypeError: person.__init__() takes 3 positional arguments but 4 were given 
#y ye error isliye dega q ki ye c ko ik argument ki tarah treat kr rha hai yani self= c
c = o


a.info()
b.info()







types of constructor
1. Default constructor --> A constructor that does not take any parameter other than self is called a default constructor.
2. parameterrized constructor --> Definition: A constructor that accepts parameters to initialize the object's data is called a parameterized