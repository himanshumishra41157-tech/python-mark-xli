# # decorator = Decorator is a function that is used to modify or extend the behavior of another function without changing
# #             its original code.


from curses import wrapper

def collage(func):
  def wrapper():
     print("welcome to sistec collage")
     func()
     print("your collage timing is :  9:10 to 4:10")
     print("75% attendence is mendetory")
  return wrapper

@collage
def CSE():
  print("welcome to cse department")

@collage
def MBA():
  print("welcome to MBA department")

@collage
def AIDS():
  print("welcome to AIDS department")


MBA()




# def greet(fx):
#   def mfx(*args, **kwargs):
#     print("Good morning")
#     fx(*args, **kwargs)
#     print("Thnaks for using our services")        #agar arguments hote hai kisi function me to hum *args and **kwargs ka use karte hai taki hum unhe access kar sake
#   return mfx


# @greet
# def hello():
#     print("Hello world")

# @greet
# def add(a, b):      
#     print(a+b)

# hello()




# add(10,20)  