dic = {
    100 : "himanshu",
    856: "ram",
    439: "shyam"}
num = int(input("enter your employe id: "))

if num in dic:
    print("welcome himanshu" , dic[num])
else:
    print("you are not employe of this company")



#value acces krne ke liye hum dictionary ke andar key ka use karte hai
info =  {""}

dic = {
    "Harry" : "himanshu"
    
    
}
print(dic["Harry"])

info = { 'name' : 'himanshu' , 'age' : 20 , 'collage' : 'iit' 
}
# print(info)
# print(info['name'])

# # agar dusre tarike se print krana hai to
# print(info.get('name')) 

# for key in info.keys() :
#     print(key)


# key values ke pair dega ye
print(info.items())

for key, value in info.items():
    print(f"the value is coresponding to the key {key} and values is {value}")