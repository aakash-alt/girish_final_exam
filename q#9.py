import numpy as np

A1=np.array([2,1,1,0,0,1]).reshape(3,2)
A2=np.array([1,1,0,1,0,1,0,1,1]).reshape(3,3)

sigma1=np.linalg.svd(A1)[1] # singular values of first matrix
sigma2=np.linalg.svd(A2)[1] # singular values of the secon matrix
infile=open('singular-values.txt','w')
print('singular values of matrix1:\t',round(sigma1[0],5),'\t',round(sigma1[1],5),file=infile)
print('singular values of matrix2:\t',round(sigma2[0],5),'\t',round(sigma2[1],5),'\t',round(sigma2[2],5),file=infile)
infile.close()
