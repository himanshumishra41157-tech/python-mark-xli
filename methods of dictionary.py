# //update method use hota hai dictionary me alag se element add krne ke liye
ep1 = {120 : 86 , 145 : 98 , 160 :85 , 165 : 45}
ep2 = {102 : 67 , 120 : 78 , 145 : 90 , 160 : 80}
ep1.update(ep2)
print(ep1)#

#clear method in python
ep1 = {120 : 86 , 145 : 98 , 160 :85 , 165 : 45}
ep2 = {102 : 67 , 120 : 78 , 145 : 90 , 160 : 80}
ep1.clear()
print(ep1)

#pop method in python jo ki use hota hai kisi bhi number ko dictionary se bahar nikalne ke liye
ep1 = {120 : 86 , 145 : 98 , 160 :85 , 165 : 45}
ep1.pop(120)
print(ep1)

#agar ham chahte hai ki bina pop item me no diye bina ki kisko hatana hai aur last ka item hat jaaye to ham ye krege
ep1 = {120 : 86 , 145 : 98 , 160 :85 , 165 : 45}
ep1.popitem()
print(ep1)
