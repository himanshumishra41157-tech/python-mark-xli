#enumerate function index deta hai
# marks = [12,56,32,98,22,45,1,4]
# index = 0
# for mark in marks:
#   print(mark)
#   if(index == 3):
#       print("Himanshu Awesome!")
#   index +=1


# for index, mark in enumerate(marks,start=1):
#     print(mark)
#     if(index==3):
#       print("Himanshu Awesome")


# Ek list mein students ke marks diye gaye hain. enumerate() ka use karke marks print karo. Jab index 3 ho, toh "Himanshu Awesome" print karo
# marks = [12,13,14,15,78,41]


# for index, mark in enumerate(marks):
#     print(mark)
#     if(index==3):
#         print("the great himanshu")



# Ek list mein students ke names hain. enumerate() aur start=1 ka use karke har student ka roll number aur name print karo.


# student_name = ["rahul" , "ram" , "Himanshu" , "Ravi"]

# for roll_no, mark in enumerate(student_name,start=1):
#       print(mark)

#       if(roll_no==3):
#           print("himanshu mishra")


# Q5. Even Index Message

# Ek list mein numbers diye hain. enumerate() with start=1 ka use karke:

# Har number print karo.

# Jab index even ho, toh "Even Position" print karo.



list1 = [10,20,30,40,50,60,70,80]

for index , mark in enumerate(list1,start=0):
    print(mark)
    if (index%2==0):
        print("even index")