letter = "Hey my name is {0} and i am from {1}"
country = "India"
name = "harry"
print(letter.format(name , country))

name = "himanshu"
country = "India"
print(f"hey my name is {name} and i am from {country}")

price = 49.998546
txt = f"the price only {price:.2f} dollers"
print(txt)
print(type(f"{2 * 40}"))