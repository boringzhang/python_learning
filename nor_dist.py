import matplotlib.pyplot as plt 
import numpy as np 
from scipy import stats
import sys

mu = 0
sigma = 0.5
x=np.arange(-5,5,0.01)
fig=plt.figure() 
ax1=fig.add_subplot(2,2,1)
ax2=fig.add_subplot(2,2,2) 
ax3=fig.add_subplot(2,2,3) 
ax4=fig.add_subplot(2,2,4) 

mu_array=[0,0,0,-2]
sigma_array=[0.5,1,5,1]
colors=["red","green","blue","m"]
gauss_labelstr='$\\alpha$=%.1g, $\\beta$=%.1g'
i=0
for mu in mu_array:
	sigma=sigma_array[i]
	y= stats.norm.pdf(x,mu,sigma)
	ax1.plot(x,y,color=colors[i], linestyle="-", label=(gauss_labelstr %(mu,sigma)))
	i+=1

ax1.legend(loc='best') 
#ax1.xlabel('x')
#ax1.ylabel('Probability density')


x=np.arange(0,20,0.1)
alpha_array=[1,2,3,5,9]
beta_array=[2,2,2,1,0.5]
colors=["red","green","blue","m","y"]
i=0
gamma_labelstr='$\\alpha$=%.1g, $\\beta$=%.1g'
for alpha in alpha_array:
	beta = beta_array[i]
	y= stats.gamma.pdf(x,alpha,0,beta)
	ax2.plot(x,y,color=colors[i], linestyle="-", label=(gamma_labelstr %(alpha,beta)))
	i+=1
ax2.legend(loc='best') 

mu = float(sys.argv[1])
sigma = float(sys.argv[2])
step=sigma/100
x=np.arange(0-sigma*4,sigma*4,step)
y= stats.norm.pdf(x,mu,sigma)
ax3.plot(x,y,color="r", linestyle="-", label=(gauss_labelstr %(mu,sigma)))
ax3.xaxis.get_major_formatter().set_powerlimits((0,1)) 
ax3.legend(loc='best') 

alpha = float(sys.argv[3])
beta = float(sys.argv[4])
step=beta/100
x=np.arange(0,beta*10, step)
y= stats.gamma.pdf(x,alpha,0,beta)
ax4.plot(x,y,color="r", linestyle="-", label=(gamma_labelstr %(alpha,beta)))
ax4.xaxis.get_major_formatter().set_powerlimits((0,1)) 
ax4.legend(loc='best') 


fig.suptitle('alpha=%f beta=%f' %(alpha,beta))
plt.show()
