# tup = (4 , 5 , 6)
# print(type(tup) , tup)

#agar hame ik element  ka tupple banana ho to
tup = (1 , 2 , 3 , 4 , "green")  #because python interpretor ko , dena padega tabhi to type = tupple dega nahi to wo type = int de dega
#tup[0] = 90
print(type(tup) , tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])

if 342 in tup:
    print("yes 342 is present in tup")
else:
    print("not avalible")

tup2 =tup[1:4]
print(tup2)