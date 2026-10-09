class math:
    def __init__(self,num):
        self.num = num

    def addtonum(self , n):
        self.num = self.num + 1


    @staticmethod
    def add(a,b):
        return a+b



a = Math(5)
print(a.num)
a.addtonum(6)
print(a.num)