#!/usr/bin/python
# -*- coding:utf-8 -*-  
from turtle import *
import numpy as np 
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg,NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter.filedialog import askopenfilename
from compiler.ast import flatten

import sys
if sys.version_info[0] < 3:
	import Tkinter as Tk
else:
	import tkinter as Tk 
	
import math

def read_file(filename):
	data=[]
	with open(filename,"r") as csvfile:
	    reader = csv.reader(csvfile)
	    for item in reader:
	    	if reader.line_num>=21:
	    		line=[]
	    		for value in item[1:]:
	    			line.append(float(value))
	    		data.append(line)
	    	if	reader.line_num>=147:
	    		break
	return data

def xy_array(filename):
	x=[]
	y=[]
	with open(filename,"r") as csvfile:
	    reader = csv.reader(csvfile)
	    for item in reader:
	    	if reader.line_num==20:
	    		line=[]
	    		for value in item[1:]:
	    			x.append(int(value))
	    	if	reader.line_num>=21 and reader.line_num<=147:
	    		y.append(int(item[0]))
	return x,y

def max_and_min(data):
	value_max = data[0][0]
	value_min = data[0][0]
	for line in data:
		if value_max<max(line):
			value_max=max(line)
		if value_min>min(line):
			value_min=min(line)
	return value_max,value_min

cdict = {'red':   [(0.0,  0.0, 0.0),
                   (0.25,  0.0, 0.0),
                   (0.5,  0.0, 0.0),
                   (0.75,  1.0,1.0),
                   (1.0,  1.0, 1.0)],

         'green': [(0.0,  0.0, 0.0),
                   (0.25,  1.0, 1.0),
                   (0.5,  1.0, 1.0),
                   (0.75,  1.0, 1.0),
                   (1.0,  0.0, 0.0)],

         'blue':  [(0.0,  1.0, 1.0),
                   (0.25,  1.0, 1.0),
                   (0.5,  0.0, 0.0),
                   (0.75,  0.0, 0.0),
                   (1.0,  0.0, 0.0)]}
def draw_pic(data,ax):
	mycm=mpl.colors.LinearSegmentedColormap("mycm",cdict)
	extent=(min(y),max(y),min(y),max(y))
	value_max,value_min= max_and_min(data)

	gci=ax.imshow(data,cmap = mycm,extent=extent, norm=mpl.colors.LogNorm(value_min,value_max))
	#配置一下坐标刻度等
	
	num=5
	tk=np.linspace(min(y),max(y),num)
	val=(max(x)-min(x))/(num-1)
	tklabels = np.arange(min(x),max(x)+1,int(val))

	ax.set_xticks(tk)
	ax.set_xticklabels(tklabels)
	ax.figure.colorbar(gci,ax=ax)  

def draw_pie(data,ax):
	fdata=flatten(data)
	i=0
	for d in fdata:
		fdata[i]=log10(d)
		i+=1
	#n, bins, patches=ax.hist(fdata,4)
	#ax.cla()
	n, bins=np.histogram(fdata,4)
	#print n
	labels= []
	i=0
	for v in bins[:-1]:
		labels.append(str('%.2e~%.2e' %(10**bins[i+1],10**v)))
		i+=1
	ax.pie(n,labels=labels,colors={'red','yellow','green','blue'},autopct='%1.1f%%')
	
if __name__ == '__main__':
	mpl.use('TkAgg')
	root=Tk.Tk()
	root.wm_title("Eye")
	root.iconbitmap('timg.ico')
	
	fig = Figure(figsize=(10,5), dpi=100)
	fig.clf()
	
	ax0 = fig.add_subplot(1,2,1)  
	ax1 = fig.add_subplot(1,2,2) 

	canvas = FigureCanvasTkAgg(fig, master=root)	
	canvas.get_tk_widget().grid(row=10, columnspan=10)   
	canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1) 

	toolbar = NavigationToolbar2TkAgg(canvas, root)
	toolbar.update()
	canvas._tkcanvas.pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
	
	filename=askopenfilename()
	#filename = "test.csv"
	#print filename
	data = read_file(filename)
	x,y = xy_array(filename)
	draw_pic(data,ax0)
	draw_pie(data,ax1)
	canvas.show()

	#启动事件循环
	root.mainloop()
