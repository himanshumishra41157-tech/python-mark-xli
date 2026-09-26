# eek(): File ke cursor ko kisi di hui position par le jaata hai. Jaise f.seek(0) cursor ko file ki shuruaat mein le jaata hai.
# tell(): Batata hai ki file ka cursor abhi kis position par hai.

with open("jara.txt" , 'r') as f :
    print(type(f))
    f.seek(10)


    data = f.read(5)

    print(data)