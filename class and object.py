class person:
    name = "Himanshu"
    occupation = "ai devloper"
    networth = 20
    def info(self):
        print(f"{self.name} is a {self.occupation}")

a = person()
b = person()
c = person()
a.name = "harsh"
a.occupation = "ca"
b.name = "khushi"
b.occupation = "IT"
a.info()
b.info()
c.info()



# print(a.name,a.occupation)