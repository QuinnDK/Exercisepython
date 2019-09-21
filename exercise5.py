#1234组成不同且不重复的三位数

for i in range(1,5):
    for k in range(1,5):
        for j in range(1,5):
            if(i!=j) and(i !=k) and (j !=k):
                print(i,k,j)