import numpy as np
modulus=4294
seed=1
a=seed # this variable contains seed=1
increment=1975
multiplier=2846


n=10000
result=[]
for i in range(n):
	seed=(multiplier*seed+increment)%modulus
	modulus+=seed
	result.append(seed)
result=np.array(result)
result=result[result==a]
if len(result)==0:
	print('seed never repeated !')
else:
	print('repeated')

