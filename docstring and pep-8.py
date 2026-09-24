# Ye kisi function, class, module ya method ke baare me explain karne ke liye likhi jaati hai.

# Docstring hamesha triple quotes (""" """ ya ''' ''') ke andar likhte hain aur function/class ki sabse pehli line me hoti hai.

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n ** 2)

square(5)

print(square.__doc__)

# Ye Python ka official style guide hai jo batata hai ki Python code kaise likhna chahiye taaki code clean, readable aur professional lage.

# Simple Example

# ❌ Wrong Style

x=10
y=20
print(x+y)

#  PEP 8 Style

x = 10
y = 20

print(x + y)