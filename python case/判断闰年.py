# #不能被100整除，能被4整除的是闰年；被400整除的也是闰年
# year=eval(input("请输入年份"))
# if((year%100!=0)&(year%4==0)):
#     print(year,"是闰年")
# elif year%400==0:
#     print(year,"是闰年")
# else:
#     print(year,"不是闰年")

#找出2000-2050年之间所有闰年，并4个一行输出
n=0
for i in range(2000,2051):
    if i%4==0 and i%100!=0 or i%400==0:
        print(i,end=" ") #end="空格“ 表示不换行
        n=n+1
        if n%4==0: #每4个输出一个换行符
            print()