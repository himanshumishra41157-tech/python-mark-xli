class  Employee:
    def __init__ (self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
            print(f"the name of the eployee is {self.name} and id is {self.id}")



e = Employee("Himanshu" , 200)
e.showDetails()
