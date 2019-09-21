#分出奇偶数

number=[12,37,5,42,8,3]
even=[]
odd=[]
for i in number:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("偶数"+str(even))
print("奇数"+str(odd))
