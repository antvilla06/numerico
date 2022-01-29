import numpy as np 
import math


#Exctract the upper triangular and lower trinagular.
A=[[2,6,7],[3,4,5],[8,13,17]]
b=[5,6,7]

U=A
for j in range(3):
    for i in range(3):
        if i>=j:
            U[i][j]=0

# Nos compute the lower triangular matrix
L = [[2,6,7],[3,4,5],[8,13,17]]

for j in range(3):
    for i in range(3):
        if i<j:
            L[i][j]=0
            
L_1=np.linalg.inv(L)
#print(L_1)

#Choose an initial value problem x_0. Make the interation
  
x_n=[0.0004,2,1]    
n=0
while n <1000:
    x_n=np.matmul(L_1,(b-np.matmul(U,x_n)))
    n = n+1

print(x_n)
    
