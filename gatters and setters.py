# # Getter ki Definition

# # Getter is a method used to get or read the value of an object's data member.

# class MyClass:
#     def __init__(self,value):
#         self._value = value


#     def show(self):
#         print(f"value is : {self._value}")

# #getter method
#     @property
#     def ten_value(self):
#         return 10* self._value


# # Setter is a method used to set or modify the value of an object's data member
#     @ten_value.setter
#     def ten_value(self,new_value):

#         self ._value =  new_value /10
        


# obj = MyClass(10)
# obj.ten_value = 67
# print(obj.ten_value)
# obj.show()







from os import name


# 🟢 Practice Question 1 — Student Marks

# Ek Student class banao.

# Requirements:

# __init__() mein name aur marks initialize karo.
# marks ko _marks ke form mein store karo.
# @property ka use karke getter banao jo marks return kare.
# setter banao jo marks ko change kare.
# Setter mein validation lagao:
# Marks 0–100 ke beech hone chahiye.
# Agar invalid marks aaye to "Invalid Marks" print ho.
# Object banao:
# s1 = Student("Himanshu", 85)
# Getter se marks print karo.
# Setter se marks ko 95 karo.
# Dobara marks print karo.



class Student:
    def __init__ (self ,  name,marks):

        self._name = name
        self._marks = marks 


    @property
    def marks(self):
         
      return self._marks

    @marks.setter
    def marks(self,new_marks):
        if 0<= new_marks <= 100:
               self._marks = new_marks
        else:
             print("Invalid marks")

s1 = Student("Himanshu" , 99)
print(s1.marks)
s1.marks = 95
print(s1.marks)


