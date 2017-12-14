from turtle import *
import os
color('red', 'red')
begin_fill()
while True:
	forward(200)
	right(144)
	if abs(pos()) < 1:
		break

end_fill()
os.system("pause")