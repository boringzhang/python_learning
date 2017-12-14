#!/usr/bin/python
# -*- coding:utf-8 -*- 
import wave
from matplotlib import pyplot as plt    
from scipy.io.wavfile import read,write
import numpy as np
filename='answer.wav'

def plot_audio(filename):
	rate,data = read(filename)
	print data
	print rate
	data=np.array(data,dtype=np.float64)
	print data
	fig = plt.figure()  
	ax1 = fig.add_subplot(1,1,1)  
	ax1.plot(data)
	plt.show()