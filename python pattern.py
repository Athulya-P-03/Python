#!/usr/bin/env python
# coding: utf-8

# In[2]:


n=5
for i in range(n):
    print("*",end="")


# In[4]:


n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print()


# In[10]:


n=5
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()


# In[13]:


n=5
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()


# In[26]:


n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
    


# In[29]:


n=5
for i in range(5):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    print()


# In[32]:


n=5
p=1
for i in range(5):
    for j in range(i+1):
        print(p,end=" ")
    p+=1
    print()


# In[36]:


n=5
p=1
for i in range(5):
    for j in range(i+1):
        print(p,end=" ")
        p+=1
    print()
        


# In[46]:


n=5
p=1
for i in range(5):
    for j in range(i,n):
        print(p,end=" ")
    p+=1
    print()
        


# In[55]:


n=5
p=5
for i in range(5):
    for j in range(i+1):
        print(p,end=" ")
    p-=1
    print()
        


# In[57]:


n=5
p=0
for i in range(5):
    for j in range(i,n):
        print(p,end=" ")
    p+=2
    print()
        


# In[60]:


n=5
p=0
for i in range(5):
    for j in range(i+1):
        print(p,end=" ")
        p+=2
    print()


# In[61]:


n=5
p=0
for i in range(5):
    for j in range(i+1):
        print(p,end=" ")
    p+=2
    print()


# In[ ]:




