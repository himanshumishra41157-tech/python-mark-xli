# a = 4
# b = "4"

# print(a is b)  # exact location of object in memory
# print(a == b)  #value


# a = [1,2,3,4,5]
# b = [1,2,3,4,5]


# print(a is b)  #cuz here he judge through the memory not by the value
# print(a==b)



#here is the main twist

# a = 3
# b = 3
# print(a is b)
# print(a = b)


# output both are true cuz 3 constant hai and immutable hai jisse python inko ik hi memory location pe locate krega



a = "himanshu"
b = "himanshu"

print( a is b)
print(a == b)