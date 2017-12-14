from turtle import *
from scipy import stats
import numpy as np 
import matplotlib.pyplot as plt 
import matplotlib.mlab as mlab

value = []
for line in open("rand1.txt"):  
	val=float(line)
	value.append(val)
	


min=-10
max=10
n=100
b=np.arange(-5,5,0.5)
a=[]
for x in b:
	a.append(0)
i=0
for v in value:
	i+=1
	if i>100000:
		break
	j=0
	for x in b:
		if v<x:
			a[j]+=1
			break
		j+=1
#print(a)
norm=stats.norm.fit(value)
mean=norm[0]
sigma=norm[1]
fig=plt.figure()  

ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2)  
ax3=fig.add_subplot(2,2,3) 
ax4=fig.add_subplot(2,2,4) 
fig.suptitle('mean=%f sigma=%f' %(mean,sigma))
ax1.plot(b,a)
ax1.grid(True)
n, bins, patches=ax2.hist(value,bins=100)

ax3.plot(bins[1:],n)
ax3.grid(True)

ax4.hist2d(value,np.random.randn(len(value)),bins=20)
plt.show()



