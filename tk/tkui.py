#!/usr/bin/python
# -*- coding:utf-8 -*-  
from tkinter import *

root = Tk()
login='�ʺ� :'
psword='���� :'
login=login.decode("gbk")
psword=psword.decode("gbk")

Label(root,text=login,).grid(row=0,column=0) # ��Label���ݽ��� ���ʽ ����
Label(root,text=psword).grid(row=1,column=0)

v1=StringVar()    # ���ñ��� . 
v2=StringVar()

e1 = Entry(root,textvariable=v1)            # ���ڴ��� ���������  
e2 = Entry(root,textvariable=v2,show='$')
e1.grid(row=0,column=1,padx=10,pady=5)      # ���б��ʽ���� . 
e2.grid(row=1,column=1,padx=10,pady=5)
def show():
    print("�ʺ� :%s" % e1.get().encode("gbk"))          # get �������� 
    print("���� :%s" % e2.get().encode("gbk"))

Button(root,text='֥�鿪��'.decode("gbk"),width=10,command=show).grid(row=3,column=0,sticky=W,padx=10,pady=5)  # ���� button ָ�� ��� , ���� ���� ���� , ʹ�ñ��ʽ���� . 
Button(root,text='�˳�'.decode("gbk"),width=10,command=root.quit).grid(row=3,column=1,sticky=E,padx=10,pady=5)

mainloop()