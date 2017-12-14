"""
Created on Mon Dec 07 16:34:10 2015

@author: SuperWang
"""

import matplotlib.pyplot as plt
import numpy as np
import time
def dynamic():
	fig,ax=plt.subplots()

	y1=[]
	y2=[]

	for i in range(100):
	    y1.append(np.sin(i*0.1))
	    y2.append(np.cos(i*0.1))
	    ax.cla()
	    ax.set_title("Loss")
	    ax.set_xlabel("Iteration")
	    ax.set_ylabel("Loss")
	    if i< 30:
	    	ax.set_xlim(0,50)
	    else:
	    	ax.set_xlim(i-30,i+20)
	    #ax.set_ylim(-1,1)
	    ax.grid()
	    ax.plot(y1,label='train')
	    ax.plot(y2,label='test')
	    ax.legend(loc='best')
	    
	    plt.pause(0.001)

dynamic()
raw_input("press any key to exit")