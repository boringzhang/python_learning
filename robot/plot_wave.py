#!/usr/bin/python
# -*- coding:utf-8 -*-  
from matplotlib import pyplot as plt     
from matplotlib import animation     
import numpy as np
from pyaudio import PyAudio, paInt16
import time


NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
TIME_SCALE = 5

def init():   
    print "init"
    line.set_data(np.linspace(0,TIME_SCALE,SAMPLING_RATE*TIME_SCALE),np.linspace(0,0,SAMPLING_RATE*TIME_SCALE))     
    return line

def animate(i):
		#print "i",i
		string_audio_data = stream.read(NUM_SAMPLES)
		audio_data = np.fromstring(string_audio_data, dtype=np.short)
		#print "audio_data",audio_data
		#print "time",time.time()
		x,y=line.get_data()
		if i*NUM_SAMPLES/SAMPLING_RATE <= TIME_SCALE:
			x=np.linspace(0, TIME_SCALE,SAMPLING_RATE*TIME_SCALE)
		else:
			start=i*NUM_SAMPLES/SAMPLING_RATE-5
			x=np.linspace(0+start, TIME_SCALE+start,SAMPLING_RATE*TIME_SCALE)
		y=np.append(y,audio_data)
		y=y[NUM_SAMPLES:]
		ax1.axis([min(x),max(x),min(y),max(y)])
		line.set_data(x, y)
		return line


pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
              frames_per_buffer=NUM_SAMPLES)

fig = plt.figure()  
ax1 = fig.add_subplot(1,1,1)   

line, = ax1.plot([], [], lw=2)  
data=[]

anim1=animation.FuncAnimation(fig, animate, init_func=init, interval=10)    
plt.show()
plt.close()