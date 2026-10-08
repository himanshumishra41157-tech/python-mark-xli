# Access modifiers are used to control the accessibility of variables, methods, and attributes inside a class.


# class Employee:
#     def __init__ (self):
#         self.__name = "Harry"


# a = Employee()
# print(a.__name)   this fucking code is not running and show the error object has no attribute __name cux here we use after . , __



class Employee:
    def __init__ (self):
        self.__name = "Harry"


a = Employee()
print(a._Employee__name) 

print(a.__dir__())      

  #here we use the Employee class in the middle of the a.__name    print(a.__name)    it sgows error

# 🔐 Name Mangling — Definition

# Name Mangling Python ka ek mechanism hai jisme double underscore (__) se start hone wale class attributes/methods ke 
# naam ko Python internally modify kar deta hai,
# taaki unhe class ke bahar directly access karna difficult h