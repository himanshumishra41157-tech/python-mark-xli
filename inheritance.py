class  Employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
            print(f"the name of the eployee is {self.name} and id is {self.id}")
#from here we use the inheritance concept to create a new class which will inherit the properties of the employee class
class programmer(Employee):
     def showlanguage(self):
          print("python is a greate language")




e = Employee("Himanshu" , 200)
e.showDetails()
e = programmer("tINA" , 4000)
e.showDetails()
e.showlanguage()
    