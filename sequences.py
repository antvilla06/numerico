import numpy as np
import math
#for i in range(0,4):
 # print(i)

#n=1
#m=1
#for k in range(0,10):
 #   n = n + m 
  #  print(n)
   # m = n + m
    #print(m)



n = 1
m=0
while n < 6:
  n = n+1
  m=n+m
print(m)


# Calcular la suma de 1/(n+1) + 1/(n+2)+ 1/(n+3)+ 1/(n+4)+...1/3n


from fractions import Fraction
k=0
n = 1000
m =0
while k < 2*1000:
  n = n+1
  m = 1/n+m 
  k= k+1 

print(m)
  
