# coutries = ("pakistan" , " afganistan" , "bangladesh" , "shrilanka")
# coutries2 = ("vietnam" , "india" , "china")
# southeastasia = coutries + coutries2
# print(southeastasia)

#count method in python
tuple1 = (0 , 1 , 2 , 3 , 2 , 3 , 1 , 3 , 2 , 3)
res = tuple1.count(3)
print("count of 3 in tuple1" , res)
#index method in python   ye method batata hai ki number konsi index par aa rha hai
tuple1 = (0 , 1 , 2 , 32 , 2 , 3 , 1 , 3 , 2 , 3)
res = tuple1.index(3 , 4 , 8)
print("count of 3 in tuple1" , res)