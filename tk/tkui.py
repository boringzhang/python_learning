#!/usr/bin/python
# -*- coding:utf-8 -*-  
from tkinter import *

root = Tk()
login='帐号 :'
psword='密码 :'
login=login.decode("gbk")
psword=psword.decode("gbk")

Label(root,text=login,).grid(row=0,column=0) # 对Label内容进行 表格式 布局
Label(root,text=psword).grid(row=1,column=0)

v1=StringVar()    # 设置变量 . 
v2=StringVar()

e1 = Entry(root,textvariable=v1)            # 用于储存 输入的内容  
e2 = Entry(root,textvariable=v2,show='$')
e1.grid(row=0,column=1,padx=10,pady=5)      # 进行表格式布局 . 
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("帐号 :%s" % e1.get().encode("gbk"))          # get 变量内容 
    print("密码 :%s" % e2.get().encode("gbk"))

Button(root,text='芝麻开门'.decode("gbk"),width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)  # 设置 button 指定 宽度 , 并且 关联 函数 , 使用表格式布局 . 
Button(root,text='退出'.decode("gbk"),width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)

mainloop()