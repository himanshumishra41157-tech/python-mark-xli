# a = input("enter the numbers: ")
# print(f"multiplication table of {a} is:")
# #if agagr hame lage ki error aane ki sambhawna hai to hum try and except ka use karenge
# try:
#    for i in range (1,11):
#     print(f"{a} x {i} =  {int(a)*i}")
# except Exception as e:
#   print("error is " ,e)






# print("some lines of code")
# print("end of the program")

#'''THE MORAL IS IF WE GET ERROR IN A PROGRAM AND WE THINk avoiding the error and print thr second program or the print value 
#  so we use try: and except''''''
try:
  num  = int(input("enter the number: "))
  a = [6,3]
  print(a[num])
except ValueError:
    print("number entered is not an integer")