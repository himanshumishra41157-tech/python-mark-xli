# # Constructor is a special method in a class that is automatically called when an object is created.
#  It is mainly used to initialize the object's data members.

class person:
    def __init__(self):
        print("Hey i am a person")
        #self name = name


    def info(self):
        print("f{self.name} is a {self.occupation}")


a = person()
b = person()