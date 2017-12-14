from turtle import *
import random
import os,sys
getscreen().bgcolor("black")
speed(0)
hideturtle()
color("green","green")
hideturtle()
Turtle().screen.delay(0)
pd()

def draw_ax(x,y,len):
	home()
	while True:
		setpos(x,y)
		forward(len)
		left(30)
		if heading() == 0:
			break

draw_ax(0,0,300)
home()

def draw_circle(x,y,radius):
	setpos(0,0-radius)
	circle(radius)

draw_circle(0,0,50)
draw_circle(0,0,100)
draw_circle(0,0,150)
draw_circle(0,0,200)
draw_circle(0,0,280)

pu()
cnt=0

def view_bar(num, total): 
	line=60
	rate = num / total 
	rate_num = rate * 100
	cnt=int(line*rate)
	r = '[%s%s]%.2f%%\r' % ("="*cnt, " "*(line-cnt), rate_num) 
	sys.stdout.write(r) 
	sys.stdout.flush() 


num=1000000
fp=open("rand1.txt")
for line in fp:  
	val=float(line)
	setpos(val*100,random.gauss(0, 1)*100)
	dot(4) 
	cnt +=1
	if cnt%100==0:
		view_bar(cnt,num)

os.system("pause")

