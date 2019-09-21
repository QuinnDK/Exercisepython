#从键盘输入一个整数。如果该数是奇数，计算alist中所有奇数的和，并将该和值加到列表的末尾；
#如果为偶数，则计算alist中所有偶数的和并加到列表末尾。
#输出最终的alist。


alist = [12, 34, 51, 66, 31, 7, 87, 58, 92]
print("请输入一个数：")
m = int(input()) #接受输入的数字并将其转换为int型
n = m%2 #判断其是奇数还是偶数
sum = 0 #预设sum为0
for i in alist: #遍历alist
    if i%2 == n: #选择与输入数奇偶性相同的数
        sum += i #累加到sum里
alist.append(sum) #将sum添加到alist的末尾
print(alist) #打印alist