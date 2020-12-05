# coding: utf-8

# In[59]:


from numpy import *
from scipy import linalg
import matplotlib.pyplot as plt


# In[60]:


a, b, h = -5, 5, 0.01
h1 = 1.0/h
A = 4
k = 0.001
J = floor((b-a)*h1)
l = A*k*h1
N =1600


# In[61]:


p = []
j=0
while j<=J:
      x = -5+(j*h)
      p.append(x)
      #print(p)
      j = j+1


# In[62]:


def g(x):
    if abs(x) <= 1:
        a = 1.0 - abs(x)
    else:
        a = 0
    return a


# In[63]:


u = []
j = 0
while j<=J:
    x = a+j*h
    aux = g(x)
    u.append(aux)
    j = j + 1

plt.plot(p,u)
plt.show()


# In[64]:


def renglon(i):
    j = 0
    auxBTBS=[]
    while j <= J:
        if j == i:
            auxBTBS.append(1.0-l)
        elif j == i-1:
            auxBTBS.append(l)
        else :
            auxBTBS.append(0.0)
        j = j + 1
    return auxBTBS


# In[65]:


BTBS = []
i = 0
while i <= J:
    aux = renglon(i)
    #print aux
    BTBS.append(aux)
    i = i+1
print (BTBS)

BTBSi = linalg.inv(BTBS)
#print (BTi)


# In[68]:


j=0
while j<=N:   
     u = matmul(BTBSi,u)
     #print (u)
     #plt.plot(p,u)
     #plt.show ()
     j = j+1


# In[67]:


plt.plot(p,u)
plt.show()
