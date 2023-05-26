# import math
# a=eval(input("请输入二次项系数："))
# b=eval(input("请输入一次项系数："))
# c=eval(input("请输入常数项："))
# der=b**2-4*a*c
# if der<0:
#     print("方程无根！")
# elif der==0:
#     x1=(-b+math.sqrt(der))/(2*a)
#     print("方程有两个相同的根：",x1)
# else:
#     x1=(-b+math.sqrt(der))/(2*a)
#     x2=(-b-math.sqrt(der))/(2*a)
#     print("方程有两个不同的根，分别是：{},{}".format(x1,x2))
import math


def bc(x1,y1,x2,y2):
    x=(x1-x2)**2
    y=(y1-y2)**2
    t=math.sqrt(x+y)
    return t

xa,ya=1,1
xb,yb=4,7
xc,yc=-2,5
b=bc(xb,yb,xc,yc)
a=bc(xa,ya,xc,yc)
c=bc(xb,yb,xa,ya)
p=(a+b+c)/2
s=math.sqrt(p*(p-c)*(p-a)*(p-b))
print("%.2f" %s)