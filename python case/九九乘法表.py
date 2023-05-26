for i in range(1,10):#i从1-9循环
    for j in range(1,i+1):#j从1-i循环
        print(j,"*",i,"=",i*j," ",end="")
    print()#当j=i时，输出换行