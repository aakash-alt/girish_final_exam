import numpy as np
import matplotlib.pyplot as plt

def y1x(x):
	return 1/3*(-np.exp(-100*x)+2*np.exp(-x)+2*x)
def y2x(x):
	return 1/3*(2*np.exp(-100*x)-np.exp(-x)-x)

data=np.loadtxt('q#6.dat')
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

fig=plt.figure(figsize=(12,12))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)


ax1.plot(x,y1x(x),'r',label='exact-y1')
ax1.plot(x,y1,'g',label='num-y1')
ax1.set(xlabel='$x$',ylabel='$y1(x)$')
ax1.legend(fontsize=10)


ax2.plot(x,y2x(x),'r',label='exact-y2')
ax2.plot(x,y2,'g',label='num-y2')
ax2.set(xlabel='$x$',ylabel='$y2(x)$')
ax2.legend(fontsize=10)
ax2.yaxis.tick_right()
ax2.yaxis.set_ticks_position('both')
plt.savefig('q#6.png')
plt.show()
