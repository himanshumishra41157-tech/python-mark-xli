#so today  we are discussing about the read and readlines.py

# f = open('intro1.txt' ,  'r')
# while True:
#     lines = f.readlines()
#     print(lines)
#     if not lines:
        
#        print(lines, type(lines))
#        break



# f = open('my file.txt' , 'r')
# while True:
#     line = f.readline()
#     if not line:
#      print(line, type(line))
#      break


    
    
# with open('my file.txt', 'r') as f:
#     for line in f:
#         print(line, type(line))





f = open('marks.txt', 'r')
i = 0
while True:
    i = i + 1
     
    line = f.readline()
    if not line:
            break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print("marks of student {i} is in m1 :{m1}")



    print(line, type(line))