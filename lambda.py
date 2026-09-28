#hey my name is himanshu mishra and today im starting to practice a lambda function 
'''for my better future jo ki mai apni faimly ko de skau'''


# lambda function is just like a single line expression used ton write a program

# def double(x):
#     return x*2

# print(double((5)))


double = lambda x : x*2
cube = lambda x : x*x*x
avg = lambda x,y,z : x+y+z/3
print(double(5))
print(cube(5))
print(avg(3,5,10))