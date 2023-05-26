#输入两个正整数m，n,求其最大公约数，最小公倍数
#最大公约数：辗转相除法
#最小公倍数：m*n/最大公约数
m=eval(input("请输入一个数："))
n=eval(input("请输入一个数："))
a=m
b=n
while n!=0:
    ys=m%n
    m=n
    n=ys
print("最大公约数：",m)
print("最小公倍数：",a*b/m)