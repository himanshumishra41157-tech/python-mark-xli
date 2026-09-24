def func1():
    try:
       l = [1,5,6,7,8]
       i = int(input("enter the index number:"))
       print(l[i])
       return 1
    except:
       print("some error is exist")
       return 0
    #finally hamesha execute hota hai chahe try ke andr jaaye ya except ke andr jaaye
    finally:
       print("i am always executed")
x = func1()


#MEANS FINALLY AISE KAAM KARTA HAI KI AGAR MAANE KI KOI FUNCTION YAANI KI FUNCTION AGAR EXECUTE KAR V JATA HAI TB BHI YE RETURN KREGA MAANEGA NAHI