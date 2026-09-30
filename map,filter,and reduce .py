# def cube(x):
#     return x*x*x



# print(cube(2))
# l = [1,2,3,4,5,6]


# newl = list(map(cube, l))
# print(newl)
# #map function har element par value lagata hai













# def filter_function(a):
#     return a>4
# newnewl  = list(filter((filter_function,l)))
# print(newnewl)







#reduce in python
from functools import reduce

numbers = [1,2,3,4,5]


def mysum(x,y):
    return x+y



sum = reduce(mysum,numbers)



print(sum)


#reduce value ko aage badha ke function me rkhne ka kaam krta h




#SO WELL THIS EXERCISE END HERE !!!!!!!!!!!!!!!!!!!!!!!