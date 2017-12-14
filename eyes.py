#!/usr/bin/python
# -*- coding:utf-8 -*-  
from turtle import *
import numpy as np 
import csv
import os

x=np.arange(-32,34,2)
y=np.arange(126,-128,-2)

#print("x len",len(x))
#print(x)
#
#print("y len",len(y))
#print(y)

data=[]
with open("test.csv","r") as csvfile:
    reader = csv.reader(csvfile)
    for item in reader:
    	if reader.line_num>=21:
    		for value in item[1:]:
    			data.append(float(value))
    	if	reader.line_num>=147:
    		break
#print("data len",len(data))

r=255
g=0
b=0
n=16
per=512/n
c=[]
i=0
while True:
	c.append([int(r),int(g),int(b)])
	if r>0 :
		r-=per
		g+=per
	else:
		g-=per
		b+=per
	if r<0:
		r=0
	if g<0:
		g=0
	if r==256:
		r=255
	if g==256:
		g=255
	if b==256:
		b=255
	i+=1
	if i>=16:
		break
i=0
j=0

pro1=[4.9e-01,1.0e-01,\
	5.0e-02,1.0e-02,\
	5.0e-03,1.0e-03,\
	5.0e-04,1.0e-04,\
	5.0e-05,1.0e-05,\
	5.0e-06,1.0e-06,\
	5.0e-07,1.0e-07,\
	5.0e-08,1.0e-08]
pro=[]
for p in pro1:
	pro.append(float(p))


pu()
colormode(255)
hideturtle()
speed(0)
Turtle().screen.delay(0)

def drwa_rect(x,y,width,hight):
	home()
	
	setpos(x,y)
	begin_fill()
	pd()
	forward(width)
	right(90)
	forward(hight)
	right(90)
	forward(width)
	right(90)
	forward(hight)
	pu()
	end_fill()

p1=-32*8
for cor in c:
	color((cor[0],cor[1],cor[2]))
	drwa_rect(p1,150*2,20,30)
	p1+=20

for value in data:
	index = 0
	for p in pro:
		if value > p:
			break
		index+=1
	if(index>=len(pro)):
		index=15

	color((c[index][0],c[index][1],c[index][2]))
	drwa_rect(x[i]*8,y[j]*2,16,4)
	i+=1
	if i>=len(x):
		i=0
		j+=1

os.system("pause")

