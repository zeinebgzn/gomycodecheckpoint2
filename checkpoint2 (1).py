#!/usr/bin/env python
# coding: utf-8

# In[1]:


#qst 1
f_name = input("enter first name: ")
l_name = input("enter last name: ")
print(f_name +" "+ l_name)


# In[2]:


# qst 2
n = 5
temp = str(n)
t1 = temp + temp
t2 = temp + temp + temp
result = int(n) + int(t1) + int(t2)
print(result)


# In[3]:


# qst 3
nombre = int(input("entrez un nombre: "))
if nombre%2 == 0:
    print("pair")
else:
    print("impair")


# In[1]:


# qst 4
for i in range(2000,3200,1):
    if i%7==0 and i%5!=0:
        print(i," ", end='')


# In[2]:


# qst 5
facto = 1
n = 8
for i in range(1,n+1):
    facto = facto * i
print("Le factoriel de", n, "est", facto)


# In[2]:


# qst 6
ps = input("entrez une phrase: ")
ps[0:-1:2]


# In[3]:


# qst 7
prix = int(input("enter the price: "))
if prix >= 500:
    prix = prix - prix*0.5
    print("Le nouveau prix du produit est de:",prix)
elif 200 < prix < 500:
    prix = prix - prix*0.3
    print("Le nouveau prix du produit est de:",prix)
elif prix < 200:
    prix = prix - prix*0.1
    print("Le nouveau prix du produit est de:",prix)


# In[ ]:




