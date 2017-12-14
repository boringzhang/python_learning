from turtle import *
import os
color('red', 'red')


def drwa_rect(x,y,width,hight):
	begin_fill()
	home()
	setpos(x,y)
	forward(width)
	right(90)
	forward(hight)
	right(90)
	forward(width)
	right(90)
	forward(hight)
	end_fill()
	
drwa_rect(0,0,10,20)

def draw_ax(x,y,len):
	home()
	while True:
		setpos(x,y)
		forward(len)
		print(heading())
		left(30)
		if heading() == 0:
			break

draw_ax(0,0,300)

os.system("pause")