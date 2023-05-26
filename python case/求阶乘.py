#输入一个正整数，求它的阶乘
#n!=1*2*3*...*n
#注意0！=1

# s=1
# n=eval(input("请输入一个正整数："))
# for i in range(1,n+1):
#     s=s*i
# print("{}！={}".format(n,s))

#第二种方法，用递归
def fun(n):
    if n==0:
        return 1
    else:
        return n*fun(n-1)
n=eval(input("请输入一个整数："))
s=fun(n)
print("{}!={}".format(n,s))