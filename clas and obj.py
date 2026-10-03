# Class Python mein ek blueprint/template hoti hai jiske through hum objects create karte hain. 
# Isme attributes (data) aur methods (functions) define kiye jaate hain.


# self Parameter – Definition

# Python mein self ek reference parameter hai jo current object ko refer karta hai.
# Iska use class ke andar object ke attributes aur methods ko access karne ke liye hota hai.
class person:
    name = "Himanshu"
    post = "ai devloper"
    state = "Madhya Pradesh" 
    def info(self):
        print(f"{self.name} is a {self.post} and he is form {self.state}")
a = person()

a.name = "harsh"
a.post = "web devloper"
a.state = "Maharashtra"


b.name = "khushi"
b.post = "HR"
# print(a.name , a.post , a.state)


 
a.info()
b.info()