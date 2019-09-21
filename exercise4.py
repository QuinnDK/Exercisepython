#已知字符串 a = “dUsHUsIR6cOM6”,要求 ：
#1)请将a字符串改为小写或改为大写
#2)将a字符串中的小写改为大写、大写改为小写

#(1)
a = "dUsHUsIR6cOM6"
print (a.upper() )
print (a.lower())

#(2)
b = ""
i=0
while i<len(a):
    if a[i].isupper():
        b +=a[i].lower()
    elif a[i].islower():
        b +=a[i].upper()
    elif a[i].isdigit():
        b +=a[i]
    i +=1
print(b)
