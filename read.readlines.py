#so today  we are discussing about the read and readlines.py

f = open('intro1.txt' ,  'r')
while True:
    lines = f.readlines()
    if not lines:
        
       print(lines, type(lines))
       break