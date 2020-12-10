n = 10
A = np.zeros((n,n))
for j in np.arange(n):
    for i in np.arange(n):
        if j == i and i+1 in  np.arange(n):
            A[i,j]=1
            A[i,j+1] = 2
            A[i,j-1] = 3
        else:
            A[n-1,n-1]=1
            A[n-1,n-2]=3
        
           
 
print(A)
