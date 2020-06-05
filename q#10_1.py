import numpy as np
import matplotlib.pyplot as plt

def fx(x):
	if -1<x<1:
		return 1
	else:
		return 0
def fk(k):
	if k!=0:
		return np.sqrt(2/np.pi)*np.sin(k)/k
	else:
		return np.sqrt(2/np.pi)
	
numpts=512 # no. of sampling points 
xmin,xmax=np.array([-10,10]) # interval in x-space
dx=(xmax-xmin)/(numpts-1) # sampling rate

xarr=np.zeros(numpts)
yarr=np.zeros(numpts)

for i in range (0,numpts):
	xarr[i]=xmin+i*dx
	yarr[i]=fx(xarr[i])
yfft=np.fft.fft(yarr,norm='ortho')
freq=np.fft.fftfreq(numpts,dx)
freq=2*np.pi*freq
factor=np.exp(-1j*freq*xmin)
yfft*=dx*np.sqrt(numpts/(2*np.pi))*factor
fk_exact=np.zeros(numpts)
for i in range(numpts):
	fk_exact[i]=fk(freq[i])

idx=np.argsort(freq)

fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(121)
ax2=fig.add_subplot(122)
ax1.plot(xarr,yarr,'r')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$f(x)$')
ax2.plot(freq[idx],fk_exact[idx],'g',label='exact')
ax2.plot(freq[idx],yfft[idx].real,'r',label='num')
ax2.set_xlabel('$k$')
ax2.set_ylabel('$f(k)$')
ax2.legend(fontsize=8)
ax2.yaxis.tick_right()
plt.suptitle('Fourier transform with 512 sampling points b/w [-10,10]',fontsize=8)
plt.savefig('q#10-1.png',dpi=500)
plt.show()
