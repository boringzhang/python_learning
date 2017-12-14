#!/usr/bin/python
# -*- coding:utf-8 -*-  
from turtle import *
import numpy as np 
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt  
#import seaborn as sns;sns.set()
import math

#x=np.arange(-32,34,2)
#y=np.arange(126,-128,-2)
#print x
#print y
#logv=10
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
def draw_pic(data):
	mycm=mpl.colors.LinearSegmentedColormap("mycm",cdict)
	extent=(min(y),max(y),min(y),max(y))
	value_max,value_min= max_and_min(data)
	gci=plt.imshow(data,cmap = mycm,extent=extent, norm=mpl.colors.LogNorm(value_min,value_max))

	#配置一下坐标刻度等  
	ax=plt.gca()
	num=5
	tk=np.linspace(min(y),max(y),num)
	val=(max(x)-min(x))/(num-1)
	tklabels = np.arange(min(x),max(x)+1,int(val))

	ax.set_xticks(tk)
	ax.set_xticklabels(tklabels)  
	cbar = plt.colorbar(gci)  
	plt.show()

if __name__ == '__main__':
	data = read_file("test.csv")
	x,y = xy_array("test.csv")
	draw_pic(data)
