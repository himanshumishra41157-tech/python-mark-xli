x  = int(input("enter the value of x:"))

match x:
    # if x is zero
       case 0:
        print("x is zero")
        # case with if condition
       case 4:
        print("x is four")

       case 5:
        print("x is five")

       case 6:
        print("x is six")

       case _:
        print("x is invalid")
               