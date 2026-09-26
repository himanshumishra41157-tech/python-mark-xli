# eek(): File ke cursor ko kisi di hui position par le jaata hai. Jaise f.seek(0) cursor ko file ki shuruaat mein le jaata hai.
# tell(): Batata hai ki file ka cursor abhi kis position par hai.

# with open("jara.txt" , 'r') as f :
#     print(type(f))
#     f.seek(10)
# #f. tell ye batata hai ki is time hamne kitne pe word skip kiye hai
#     print(f.tell())
#     data = f.read(5)

#     print(data)







#truncate method -- Python file handling mein truncate() file ki length set karta hai. Jo content us length ke baad hai, woh hat jaata hai.
with open("sample.txt", 'w') as f:
    f.write("hello world")


with open("sample.txt" , 'r') as f:
    print(f.read())