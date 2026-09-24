# x = 4
# print(x)

# def hello():
#     x = 5
#     print(f"the local x is {x}")
#     print("hello harry")
#     print("hello himanshu")
# print(f"the global x is {x}")
# hello()
# print(f"the global x is {x}")








# x = 10

# def my_function():
#     global x

#     x = 4
#     y = 5

#     print(y)


# my_function()
# print(x)




x = 20

def test():
    global x
    x = 10
    y = 20
    print(x)
    print(y)

test()
print(x)