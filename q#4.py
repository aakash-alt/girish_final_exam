import numpy as np
import matplotlib.pyplot as plt

numpts=1024
np.random.seed(numpts)
x=np.random.rand(1024)
plt.figure(figsize=(12,12))
plt.plot(x,'.k')
plt.xlabel('numpts')
plt.ylabel('$samples$')
plt.savefig('q4-sample.png')
plt.show()


k=np.fft.fftfreq(numpts) # k-wave vectors
print('minimun k:\t',k.min(),'\n','maximum k:\t',k.max())


# power spectrum of the sample
dft=np.fft.fft(x,norm='ortho')
ps=dft*np.conj(dft)
ps=ps.real/numpts
nbin=5
avpspec=np.zeros(204,dtype=np.complex_) # size of each bin
data=np.array_split(x[0:1020],nbin)
for i in range(nbin):
	freq=2*np.pi*np.fft.fftfreq(len(data[i]),d=1) # '1' is the step size
	dft=np.fft.fft(data[i],norm='ortho')
	pspec=dft*np.conj(dft)/len(data[i])
	avpspec=avpspec+pspec
avpspec*=1/nbin
idx2=np.argsort(freq)
plt.figure(figsize=(12,12))
plt.plot(freq[idx2],avpspec[idx2].real,'k')
plt.title('power psectrum using Bartlett method',fontsize=8)
plt.xlabel('$k$')
plt.ylabel('power-spectrum')
plt.savefig('q4-ps.png')
plt.show()
