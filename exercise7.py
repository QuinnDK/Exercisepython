#一个整数加上100后是完全平方数，再加上268又是一个平方数

import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x*x==i+100) and  (y*y==i+268):
        print(i)
