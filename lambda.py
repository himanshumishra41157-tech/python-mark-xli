#hey my name is himanshu mishra and today im starting to practice a lambda function 
'''for my better future jo ki mai apni faimly ko de skau'''


# lambda function is just like a single line expression used ton write a program

# def double(x):
#     return x*2

# print(double((5)))


# double = lambda x : x*2
# cube = lambda x : x*x*x
# avg = lambda x,y,z : (x+y+z)/3
# #baat ye hai kio ham function ke andar bhi function likh sakte hai
# def apple(fx,value):
#     return 6+fx(value)




# print(double(5))
# print(cube(5))
# print(avg(3,5,10))

# print(apple(lambda x : x*2,2))





# Lambda tab kaam aata hai jab ek chhota function sirf ek jagah chahiye. Example: students ko marks ke hisaab se sort karna:


students = [("Aman", 75), ("Riya", 92), ("Himanshu", 81)]

students.sort(key=lambda student: student[1])

print(students)


# @lambda function se related questions ---------------------------


# Lambda se number ko square karke calculate mein bhejo.

square = lambda x: x*2
print(square(4))