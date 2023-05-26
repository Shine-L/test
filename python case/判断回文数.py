#回文数是正读反读都一样的数，如12321，121
#判断五位数是不是回文数
def ishuiwenshu(x):
    ge = x % 10
    shi = x // 10 % 10
    bai = x // 100 % 10
    qian = x // 1000 % 10
    wan = x // 10000
    # if ge==wan:
    #     if shi==qian:
    #         print(x,"是回文数")
    #     else:
    #         print(x,"不是回文数") 写成这样如果个位不等于万位也不会输出不是回文数
    if ge == wan and shi == qian:
        print(x, "是回文数")
    else:
        print(x, "不是回文数")
x=eval(input("请输入一个五位数："))
if 10000<=x<=99999:
    ishuiwenshu(x)
else:
    x=eval(input("请重新输入一个5位数："))
    ishuiwenshu(x)