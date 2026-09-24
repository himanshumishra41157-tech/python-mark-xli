questions = [
["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],
["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],


["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],

["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],

["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],


["which language is used for web devlopment?" , "python" , "c" , "c++" , "java" ,"javascript",4],




]





levels = [1000 , 2000 , 3000 ,4000, 5000 , 6000 ,7000 , 8000 , 9000 , 10000]
money = 0
for i in range(0 ,len(questions)):
    question = questions[i]
    print(f"question for Rs. {levels[i]}")
    print(f"a. {question[1]}     b. {question[2]}")
    print(f"c. {question[3]}     d. {question[4]}") 
    reply = int(input("enter your answer(1-4) or 0 to quit:"))
    if (reply == 0):
        money = levels[i-1]
        print(f"you have quitted the game and you have won rs. {money}")
        break
    if reply == question[-1]:
        print(f"your answer is corrrect and you have won rs. {levels[i]}")
        if(i == 4):
             money = 1000
        elif(i==6):
             money = 1000

    else:
        print(f"your answer is wrong and you have lost the money")
        break