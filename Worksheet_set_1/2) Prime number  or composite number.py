#!/usr/bin/env python
# coding: utf-8

# In[8]:


n= int(input("Enter the number:"))
if(n ==0 or n == 1):
    printf(n,"Number is neither prime nor composite")
elif n>1 :
    for i in range(2,n):
        if(n%i == 0):
            print(n,"This is a composite number")
            break
    else:
        print(n,"The number is prime")
else :
    print("Enter positive number")

