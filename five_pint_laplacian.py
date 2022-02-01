import numpy as np



n=5

In=-np.identity(3)
mp=np.array([[4,-1,0],[-1,4,-1],[0,-1,4]])


A=[]

for i in range(0,3*(n-1)):
    A.append([0]*3*(n-1))
    

A=np.asmatrix(A)

for k in range(0,n-1):
    A[3*k:3*k+3,3*k:3*k+3]=mp
  

if n == 2:
    print(A)
else:
    for i in range(0,n-2):
        A[3*i+3:3*i+6,3*i:3*i+3]=In
    A[3*i:3*i+3,3*i+3:3*i+6]=In
        
print(A)   

invA= np.linalg.inv(A)
