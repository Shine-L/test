#在3000-6000之间的奇数中，找出各位数字之和是30的倍数的数值,并计算这些数值之和
sum=0
for i in range(3001,6000,2):
    ge=i%10
    shi=i//10%10
    bai=i//100%10
    qian=i//1000
    s=ge+shi+bai+qian
    if s%30==0:
        print(i)
        sum=sum+i
print("sum:",sum)