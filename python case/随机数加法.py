#给小学生出4道100以内的2个数的加法题，每道题25分，根据学生答案，显示实际得分
from random import randint
i=0
score=0
answer=0
trueanswer=0
for i in range(1,5):
    op1=randint(10,99) #random.randint(a,b) 返回一个随机的整数值n,且a<=n<=b,a<b
    op2=randint(10,99)#random.uniform(a,b) 返回一个随机的介于ab之间的浮点值，若a>b,则n属于[b,a],若a<b,则n属于[a,b]
    print(op1,"+",op2,"=")
    answer=eval(input("请输入答案："))
    trueanswer=op1+op2
    if(answer==trueanswer):
        score+=25
    i+=1
print("你的得分是：",score)
