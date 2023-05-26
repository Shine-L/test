
#开始
def CaesarCipher():
    c=mingwen.get("0.0","end")
    b=''
    miwen.delete("0.0","end")
    i=0
    while not(i>=len(c)):
        if 'a'<=c[i]<='w' or 'A'<=c[i]<='W':
            b=b+chr(ord(c[i])+3)
        elif 'x'<=c[i]<='z' or 'X'<=c[i]<='Z':
            b=b+chr(ord(c[i])-23)
        else:
            b=b+c[i]
        i=i+1
    miwen.insert("0.0",b)


from tkinter import *
root=Tk()
root.title("恺撒密码")
root.geometry('300x200')
Label(root,text='请输入明文',font=('Arial',10)).pack()
mingwen=Text(root,width=300,height=4)
mingwen.pack()
mingwen.focus_set()
Button(root,text="加密",command=CaesarCipher,relief="raised",width=10).pack()
Label(root,text='恺撒密文',font=('Arial',10)).pack()
miwen=Text(root,width=300,height=4)
miwen.pack()
root.mainloop()
#结束


