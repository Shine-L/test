#自己琢磨的方法
#输出100以内的素数，素数是除了能被1和本身整除，不能被其他整数整除的数
#素数也叫质数，合数的概念和素数相反
for i in range(1,101):
    for n in range(2,i):
        if i%n==0:#判断是否能整除，能整除就跳出这个循环
            break
        elif (n==i-1):#判断从i到i-1是否所有的数都除过了
            print(i)#1不是素数，所以也不用输出1

#网上搜的
num=[];
i=2
for i in range(2,100):
  j=2
  for j in range(2,i):
   if(i%j==0):
     break
  else:
   num.append(i)
print(num)