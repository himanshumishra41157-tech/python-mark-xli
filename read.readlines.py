#so today  we are discussing about the read and readlines.py

# f = open('intro1.txt' ,  'r')
# while True:
#     lines = f.readlines()
#     print(lines)
#     if not lines:
        
#        print(lines, type(lines))
#        break



f = open('my file.txt' , 'r')
while True:
    line = f.readlines()
    if not line:
        break
    print(line)