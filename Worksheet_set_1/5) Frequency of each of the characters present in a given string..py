#!/usr/bin/env python
# coding: utf-8

# In[35]:


str = "AKANSH"
dict = {}
for i in str:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1
print(dict)

