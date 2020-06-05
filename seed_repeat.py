import numpy as np
modulus=4294
seed=1
a=seed
increment=1975
multiplier=2846


n=10000
results=[]
for i in range(n):
	seed=(multiplier*seed+increment)%modulus
	if seed==a:
		print('seed-repeated @',i,'point')
