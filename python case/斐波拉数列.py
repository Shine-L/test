#斐波那契数列（Fibonacci sequence），又称黄金分割数列，因数学家莱昂纳多·斐波那契（Leonardo Fibonacci）以兔子繁殖为例子而引入，故又称为“兔子数列”，
# 指的是这样一个数列：1、1、2、3、5、8、13、21、34、……在数学上，
# 斐波那契数列以如下被以递推的方法定义：F(0)=0，F(1)=1, F(n)=F(n - 1)+F(n - 2)（n ≥ 2，n ∈ N*）
#编程求出斐波那契数列的第几项开始大于2021（要使用函数调用）
# def fun(n):
#     if n<=2:
#         return 1
#     else:
#         return fun(n-1)+fun(n-2)
#
#
# i=1
# while fun(i)<=2021:
#     i+=1
# print("第{}项是{},大于2021".format(i,fun(i)))
#
# a=1
# b=1
# for i in range(3,51):
#     s=a+b
#     a=b
#     b=s
# print("第50位的值：",s)

f1=1
f2=1
for i in range(3,51):
    f3=f1+f2
    f1=f2
    f2=f3
print(f3)