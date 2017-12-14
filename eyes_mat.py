#!/usr/bin/python
# -*- coding:utf-8 -*-  
from turtle import *
import numpy as np 
import csv
import matplotlib as mpl
import matplotlib.pyplot as plt  
#import seaborn as sns;sns.set()
import math

x=np.arange(-32,34,2)
y=np.arange(126,-128,-2)

#print("x len",len(x))
#print(x)

#print("y len",len(y))
#print(y)

data=[]

logv=10
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for item in reader:
    	if reader.line_num>=21:
    		line=[]
    		for value in item[1:]:
    			#line.append((math.log(float(value),logv)))
    			line.append(float(value))
    		data.append(line)
    	if	reader.line_num>=147:
    		break
print("data len",len(data))
print("data[] len",len(data[0]))

value_max = data[0][0]
value_min = data[0][0]
for line in data:
	if value_max<max(line):
		value_max=max(line)
	if value_min>min(line):
		value_min=min(line)

print(value_max)
print(value_min)



#sns.heatmap(data,cmap = 'jet',norm=norm)
#sns.heatmap(data,cmap = 'rainbow')


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
mycm=mpl.colors.LinearSegmentedColormap("mycm",cdict)
#mycm=mpl.cm.jet
#print(mycm)
#mycm=mpl.colors.LinearSegmentedColormap.from_list("mycm",mpl.cm.jet(np.linspace(0, 0.9, 100)))
extent=(min(y),max(y),min(y),max(y))

gci=plt.imshow(data,cmap = mycm,extent=extent, norm=mpl.colors.LogNorm(value_min,value_max))

#配置一下坐标刻度等  
ax=plt.gca()
num=5
tk=np.linspace(min(y),max(y),num)
val=(max(x)-min(x))/(num-1)
tklabels = np.arange(min(x),max(x)+1,int(val))
#print(tk)
#print(tklabels)
ax.set_xticks(tk)
ax.set_xticklabels(tklabels)  

#num=7
#tk=np.linspace(min(y),max(y),num)
#val=(max(y)-min(y))/(num-1)
#tklabels = np.arange(min(y),max(y)+1,int(val))
#print(tk)
#print(tklabels)
#ax.set_yticklabels(tk)
#ax.set_yticklabels(tklabels)
#显示colorbar  
cbar = plt.colorbar(gci)  
##cbar.set_label('$T_B(K)$',fontdict=font)  
#tk=np.linspace(value_min,value_max,8)
#cbar.set_ticks(tk)  
#tklabels = []
#for t in tk:
#	tklabels.append(format(logv**(float(t)),'.2e'))

#cbar.set_ticklabels(tklabels) 

plt.show()


