import numpy as np
import matplotlib.pyplot as plt

def p(x):
	return 0
def q(x):
	return 4
def r(x):
	return -4*x
def y(x):
	return np.exp(2)*(np.exp(4)-1)**-1*(np.exp(2*x)-np.exp(-2*x))+x
a,b=np.array([0,1])
alpha,beta=np.array([0,2])
N=99

h=(b-a)/(N+1)
x=a+h

A=np.zeros(N+1)
B=np.zeros(N+1)
C=np.zeros(N+1)
D=np.zeros(N+1)

# preparing tidiagonal-matrix for the arosen linear system of equation
A[1]=2+h**2*q(x)
B[1]=-1+(h/2)*p(x)
D[1]=-h**2*r(x)+(1+p(x)*h/2)*alpha
for i in range (2,N):
	x=a+i*h
	A[i]=2+h**2*q(x)
	B[i]=-1+(h/2)*p(x)
	C[i]=-1-(h/2)*p(x)
	D[i]=-h**2*r(x)
x=b-h
A[N]=2+h**2*q(x)
C[N]=-1-(h/2)*p(x)
D[N]=-h**2*r(x)+(1-p(x)*h/2)*beta

# soliving of tridgoanal-matrix
l=np.zeros(N+1)
u=np.zeros(N+1)
z=np.zeros(N+1)

l[1]=A[1]
u[1]=B[1]/A[1]
z[1]=D[1]/l[1]
for i in range(2,N):
	l[i]=A[i]-C[i]*u[i-1]
	u[i]=B[i]/l[i]
	z[i]=(D[i]-C[i]*z[i-1])/l[i]
l[N]=A[N]-C[N]*u[N-1]
z[N]=(D[N]-C[N]*z[N-1])/l[N]

w=np.zeros(N+2)
w[0],w[N+1],w[N]=np.array([alpha,beta,z[N]])
for i in range(N-1,0,-1):
	w[i]=z[i]-u[i]*w[i+1]
X=np.zeros(N+2)
for i in range(0,N+2):
	X[i]=a+i*h
	#print(X[i],w[i])
fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(111)
ax1.plot(X,y(X),'r',label='exact')
ax1.plot(X,w,'m',label='num')
ax1.set_xlabel('$x$')
ax1.set_ylabel('$y(x)$')
ax1.legend(fontsize=10)
plt.savefig('q#8.png')
plt.show()
