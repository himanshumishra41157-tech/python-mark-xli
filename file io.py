# agar hame kisi file ko open krke usko read krna hoto ham phle ik file 
# banayege jisme data text ke taur par hoga and then usko f ya kisi bhi variable se assign krege after this isme ham f = open('my file.txt , 'r') f.read()
# f = open('my file.txt' , 'r')
# # f = open('my file.txt' , 'r')   #agar ham yaha bina r mode ke kare tb bhi chlega  q ki r mod fefault hota hai
# text = f.read()

# print(text)
# f.close()

#for write inside the file
f = open('my file2.txt' , 'w')
text = f.write('Helllo ! himanshu')

f.close()







#agar hame without  close statement ka use kre file likhni hai  to ham with statement ka use krege
with open('my file.txt' ,  'a'):
    f.write("hey im inside with") 








