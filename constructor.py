# # Constructor is a special method in a class that is automatically called when an object is created.
#  It is mainly used to initialize the object's data members.

class person:
    def __init__(self , n , o):
        print("Hey i am a person")
        self.name = n
        self.occupation = o


    def info(self):
        print(f"{self.name} is a {self.occupation}")


a = person("Harry" , "AI devloper")
b = person("Divya" , "Web devloper")
c =  person()


a.info()
b.info()