#输入年月日，输出属于该年的第几天
#要判断是闰年还是平年，闰年有366天，平年有365天
#闰年：1.能被4整除，但是不能被100整除，2.能被400整除，满足其中之一个条件即可
s=0
year=eval(input("请输入年份："))
month=eval(input("请输入月份："))
date=eval(input("请输入日期："))
day=[31,28,31,30,31,30,31,31,30,31,30,31]
for i in range (1,month):
    s=s+day[i-1]#计算已经过去的月份
s=s+date
if (year%4==0 and year%100!=0) or year%400==0:
    if month>2:
        s=s+1
print("{0}/{1}/{2}是{0}年中第{3}天".format(year,month,date,s))

