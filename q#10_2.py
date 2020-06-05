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
	
numpts1=512
numpts2=2*numpts1
numpts3=4*numpts1
xmin,xmax=np.array([-10,10]) 
dx1=(xmax-xmin)/(numpts1-1) 
dx2=(xmax-xmin)/(numpts2-1) 
dx3=(xmax-xmin)/(numpts3-1) 

xarr1=np.zeros(numpts1)
yarr1=np.zeros(numpts1)
xarr2=np.zeros(numpts2)
yarr2=np.zeros(numpts2)
xarr3=np.zeros(numpts3)
yarr3=np.zeros(numpts3)

for i in range (0,numpts1):
	xarr1[i]=xmin+i*dx1
	yarr1[i]=fx(xarr1[i])
for i in range (0,numpts2):
	xarr2[i]=xmin+i*dx2
	yarr2[i]=fx(xarr2[i])
for i in range (0,numpts3):
	xarr3[i]=xmin+i*dx3
	yarr3[i]=fx(xarr3[i])
yfft1=np.fft.fft(yarr1,norm='ortho')
freq1=np.fft.fftfreq(numpts1,dx1)
freq1=2*np.pi*freq1
factor1=np.exp(-1j*freq1*xmin)
yfft1*=dx1*np.sqrt(numpts1/(2*np.pi))*factor1

yfft2=np.fft.fft(yarr2,norm='ortho')
freq2=np.fft.fftfreq(numpts2,dx2)
freq2=2*np.pi*freq2
factor2=np.exp(-1j*freq2*xmin)
yfft2*=dx2*np.sqrt(numpts2/(2*np.pi))*factor2

yfft3=np.fft.fft(yarr3,norm='ortho')
freq3=np.fft.fftfreq(numpts3,dx3)
freq3=2*np.pi*freq3
factor3=np.exp(-1j*freq3*xmin)
yfft3*=dx3*np.sqrt(numpts3/(2*np.pi))*factor3


fk_exact=np.zeros(numpts1)
for i in range(numpts1):
	fk_exact[i]=fk(freq1[i])

idx1=np.argsort(freq1)
idx2=np.argsort(freq2)
idx3=np.argsort(freq3)

fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(111)
ax1.plot(freq1[idx1],fk_exact[idx1],'r',label='exact')
#ax1.plot(freq1[idx1],yfft1[idx1].real,'g',label='num-dx=%f'%(dx1))
#ax1.plot(freq2[idx2],yfft2[idx2].real,'b',label='num-dx=%f'%(dx2))
ax1.plot(freq3[idx3],yfft3[idx3].real,'m',label='num-dx=%f'%(dx3))
ax1.set_xlabel('$k$')
ax1.set_ylabel('$f(k)$')
ax1.legend(fontsize=8)
ax1.yaxis.tick_right()
#plt.savefig('q#10-4.png',dpi=500)
plt.show()
