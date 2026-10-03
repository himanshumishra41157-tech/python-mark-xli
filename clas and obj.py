# Class Python mein ek blueprint/template hoti hai jiske through hum objects create karte hain. 
# Isme attributes (data) aur methods (functions) define kiye jaate hain.
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

# print(a.name , a.post , a.state)
a.info()