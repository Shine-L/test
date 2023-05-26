# def match_num(num):
#     f=[6,2,5,5,4,5,6,3,7,6]
#     if num==0:
#         total=f[0]
#     else:
#         total=0
#
#     while(num>0):
#         x=num%10
#         total=total+f[x]
#         num=num//10
#     return total



import hanshu
a=int(input("请输入数字："))
b=hanshu.match_num(a)
print(b)