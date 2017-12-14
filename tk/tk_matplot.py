#!/usr/bin/env python
#coding:utf-8
"""
  Author:  Chaos --<Chaosimpler@gmail.com>
  Purpose: �޸�Matplotlib�ĺ�ˣ�ʵ����Tkinter��GUI����ͼ��
  Created: 2014-10-15
"""
import numpy as np
from Tkinter import *
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
 
#----------------------------------------------------------------------
def drawPic():
	"""
	��ȡGUI�������õĲ��������øò�������ͼƬ
	"""
	
	#��ȡGUI�����ϵĲ���
	try:sampleCount=int(inputEntry.get())
	except:
		sampleCount=50
		print '����������'
		inputEntry.delete(0,END)
		inputEntry.insert(0,'50')
	
	#���ͼ����ʹ��ǰ�����λ��Ƶ�ͼ�񲻻��ص�
	drawPic.f.clf()
	drawPic.a=drawPic.f.add_subplot(111)
	
	#��[0,100]��Χ���������sampleCount�����ݵ�
	x=np.random.randint(0,100,size=sampleCount)
	y=np.random.randint(0,100,size=sampleCount)
	color=['b','r','y','g']
	
	#������Щ������ɢ��ͼ����ɫ���ѡȡ
	drawPic.a.scatter(x,y,s=3,color=color[np.random.randint(len(color))])
	drawPic.a.set_title('Demo: Draw N Random Dot')
	drawPic.canvas.show()
	
def dynamic():
	try:sampleCount=int(inputEntry.get())
	except:
		sampleCount=50
		print '����������'
		inputEntry.delete(0,END)
		inputEntry.insert(0,'50')
	drawPic.f.clf()
	drawPic.a=drawPic.f.add_subplot(111)
	ax = drawPic.a

	y1=[]
	y2=[]
	
	ax.set_ylim(-1,1)
	for i in range(sampleCount):
		y1.append(np.sin(i*0.1))
		y2.append(np.cos(i*0.1))
		ax.cla()
		ax.plot(y1,label='train')
		ax.plot(y2,label='test')
		ax.set_title("Loss")
		ax.set_xlabel("Iteration")
		ax.set_ylabel("Loss")
		ax.legend(loc='best')
		ax.grid()

		ax.set_ylim(-1,1)
		
		if i< 30:
			ax.set_xlim(0,50)
		elif (sampleCount-i) < 20:
			if sampleCount-50>=0:
				ax.set_xlim(sampleCount-50,sampleCount)
			else:
				ax.set_xlim(0,50)
		else :
			ax.set_xlim(i-30,i+20)
		
		

		drawPic.canvas.show()
		#plt.pause(0.001)

if __name__ == '__main__':
	
	matplotlib.use('TkAgg')
	root=Tk()
	
	#��Tk��GUI�Ϸ���һ������������.grid()����������
	drawPic.f = Figure(figsize=(5,4), dpi=100) 
	drawPic.canvas = FigureCanvasTkAgg(drawPic.f, master=root)
	drawPic.canvas.show()
	drawPic.canvas.get_tk_widget().grid(row=0, columnspan=3)    
 
	#���ñ�ǩ���ı���Ͱ�ť�Ȳ������������ı����Ĭ��ֵ�Ͱ�ť���¼�����
	Label(root,text='����������������'.decode('gbk')).grid(row=1,column=0)
	inputEntry=Entry(root)
	inputEntry.grid(row=1,column=1)
	inputEntry.insert(0,'50')
	Button(root,text='��ͼ'.decode('gbk'),command=dynamic).grid(row=1,column=2,columnspan=3)
	
	#�����¼�ѭ��
	root.mainloop()