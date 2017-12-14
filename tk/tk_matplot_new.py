#!/usr/bin/env python
#coding:utf-8
"""
"""
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib import animation  
import sys
if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk 
#----------------------------------------------------------------------
def init():    
	line.set_data(0,0)    
	line2.set_data(0,0)    
	return line,line2  
  
# animation function.  this is called sequentially     
def animate(i):
	x = np.arange(0, i, 0.1) 
	y = np.sin(x * 0.1) 
	line.set_data(x,y)     
 
	y2 = np.cos(x*0.1)    
	line2.set_data(x,y2) 

	#print sampleCount,i
	if i< 50:
		ax.set_xlim(0,50)
	else :
		ax.set_xlim(i-50,i)
 
	return line,line2  

def dynamic():
	try:
		sampleCount=int(inputEntry.get())
	except:
		sampleCount=50
		print '����������'
		inputEntry.delete(0,END)
		inputEntry.insert(0,'50')

	anim1=animation.FuncAnimation(fig, animate, init_func=init,  frames=sampleCount, interval=10,repeat=False)
	canvas.show()
def Exit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate
if __name__ == '__main__':
	
	matplotlib.use('TkAgg')
	root=Tk.Tk()
	root.wm_title("Embedding in TK")
	
	#��Tk��GUI�Ϸ���һ������������.grid()����������

	fig = Figure(figsize=(5,4), dpi=100) 
	fig.clf()
	
	ax = fig.add_subplot(1,1,1)  
	#ax2 = fig.add_subplot(1,2,2)  
	ax.grid()
	ax.set_ylim(-1,1)
	ax.set_xlim(0,50)
	ax.set_title("Loss")
	ax.set_xlabel("Iteration")
	#ax.set_ylabel("Loss")

	line, = ax.plot([],label='sin')    
	line2, = ax.plot([],label='cos')  
	ax.legend(loc='best')
	
	canvas = FigureCanvasTkAgg(fig, master=root)	
	canvas.show()
	canvas.get_tk_widget().grid(row=10, columnspan=10)   
	toolbar = NavigationToolbar2TkAgg(canvas, root)
	toolbar.update()
	canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1) 
	
	buttonExit=Tk.Button(root,text='�˳�'.decode('gbk'),command=Exit)
	

	button=Tk.Button(root,text='��ͼ'.decode('gbk'),command=dynamic)
	

	
	#���ñ�ǩ���ı���Ͱ�ť�Ȳ������������ı����Ĭ��ֵ�Ͱ�ť���¼�����
	lable = Tk.Label(root,text='����������������'.decode('gbk'))
	
	inputEntry=Tk.Entry(root)
	
	sampleCount = 50
	inputEntry.insert(0,'50')
	inputEntry.pack(pady=20,side=Tk.LEFT,fill=Tk.X,expand=1) 
	lable.pack(pady=20,side=Tk.RIGHT,fill=Tk.X,expand=1) 
	buttonExit.pack(side=Tk.BOTTOM,expand=1)
	button.pack(side=Tk.BOTTOM,expand=1)
	


	
	

	#�����¼�ѭ��
	root.mainloop()