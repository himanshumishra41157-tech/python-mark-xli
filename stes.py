# s = {2,4,2,6}
# print(s)

# info = {"carla" , 1.9 , False , 19}
# print(info)

# himanshu = set()
# print(type(himanshu))


# for value in info:
#     print(value)


#sets method in python 
#UNION method in python
# s1 = {1, 2  , 5 , 6}
# s2 = {3 , 6 , 7 }
# print(s1.union(s2))

#intersection method in python
# c1 = {"delhi" , "mumbai" , "kolkata"}
# c2 = {"delhi" , "mumbai" , "chennai"}
# print(c1.intersection(c2))

#agar hame diffrerence dikhana ho to ham use krege symmetric_difference method in python
c1 = {"delhi" , "mumbai" , "kolkata"}
c2 = {"delhi" , "mumbai" , "chennai"}
print(c1.symmetric_difference(c2))

#disjoint method in python
#agar hame ye check karna ho ki dono sets me koi common element hai ya nahi
c1 = {"delhi" , "mumbai" , "kolkata"}
c2 = {"delhi" , "mumbai" , "chennai"}
print(c1.isdisjoint(c2))

#superset method in python
#agar hame ye check karna ho ki c1 set c2 ka superset hai MEANS c1 me c2 ke sare elements hai ya nahi to hum superset method ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c2 = {"delhi" , "mumbai" , "chennai"}
print(c1.issuperset(c2))

#subset method in python
#agar hame ye check karna ho ki c1 set c2 ka subset hai means agar hame ye check krna ho kic1 ki jo bhi elements hai kya wo c2 me hai ya nahi to hum subset method ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c2 = {"delhi" , "mumbai" , "chennai"}
print(c1.issubset(c2))

#add method in python
#agar hame set me koi bhi element add karna ho to hum add method ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c1.add("jhansi")
print(c1)
#update method in python
#agar hame set me ek se jyada element add karna ho to hum update method ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c2 = {"delhi" , "mumbai" , "chennai" , "rampur"}
c1.update(c2)
print(c1)

#remove method in python
#agar hame set me se koi bhi element remove karna ho to hum remove method ka
c1 = {"delhi" , "mumbai" , "kolkata"}
c1.remove("delhi")
print(c1)

#discard method in python
#agar hame set me se koi bhi element remove karna ho to hum discard method ka without error ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c1.discard("delhi2")
print(c1)

#pop method in python
#agar hame kisi bhi set se koi bhi element ko bracet ke baahr nikalna ya pop karna ho to hum pop method ka use karenge
c1 = {"delhi" , "mumbai" , "kolkata"}
c1.pop()
print(c1)   

#Del method in python
#agar hame kisi bhi set ko delete karna ho to hum del method ka use kar karenge
# c1 = {"delhi" , "mumbai" , "kolkata"}
# del c1
# print(c1)

#ye error through krega
#clear method in python
#agar hame kisi bhi set ke sare elements ko clear karna ho to hum clear method ka use karenge
c1 = {"delhi" , "mumbai" , "raipur"}
c1.clear()
print(c1)