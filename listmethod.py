#append method in python --
#ye wo method hota hai jo list ke aakihiri me append method call karne par aakhiri me koi bhi number add kar dega 
l = [1, 2 , 3 , 4 , 5 , 6 ]
print(l)
l.append(7)
print(l)

#sort method in python --
#ye wo method hota hai jo list ke elements ko ascending order me sort kar deta hai
l = [11, 2 , 3 , 45 , 5 , 6]
l.sort()
print(l)

#agar desemding order me sort karna ho to hum sort method ke andar reverse = True likh denge
L = [11, 2 , 3 , 45 , 5 , 6]

L.sort(reverse = True)
print(L)

#REVERSE method in python --
#ye wo method hota hai jo list ke elements ko reverse kar deta hai
l = [11, 2 , 3 , 45 , 5 , 6]
l.reverse()
print(l)

#index method in python --
#ye wo method hota hai jo list ke elements me se kisi bhi element ka index return kar deta hai
l = [11, 2 , 3 , 45 , 5 , 6]
print(l.index(3))

#count method in python --
#is method ka kaam ye hai ki ye list ke kisi bhi element ka count return kar deta hai ki ye number list me kitni baar aaya hai
l = [ 12 , 2 , 44 , 2 , 3 , 45 , 5 , 6]
print(l.count(2))

#copy method in python --
#ye wo method hota hai jo list ke elements ko copy kar deta hai
l = [ 12 , 3 , 43 , 45 , 5 , 6]
l = l.copy()
print(L)


#insert method in python --
#ye wo method hota hai jo list ke elements me se kisi bhi index par koi bhi element insert kar deta hai
l = [ 13 , 32 , 2 , 43 , 21 , 41]
l.insert(2, 40)
print(l)

#extend method in python
# ye wo method hai jo m ko l ke end me add kr deta hai
l = [ 11, 12 , 14 , 44 , 56]
print(l)
m = [900 , 1000 , 1100]
l.extend(m)
print(l)