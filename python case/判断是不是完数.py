#如果一个数等于它的因子之和，这个数就是完数，如6的因子是1，2，3，且6=1+2+3
x=eval(input("请输入一个整数："))
num=[]
sum=0
for n in range(1,x):
    if x%n==0:
        num.append(n)#将因数存入数组
i= len(num)#i是数组的长度
for a in range(0,i):
    sum=sum+num[a]#将因数相加
if sum==x:
    print(x,"是完数")
else:
    print("不是完数")