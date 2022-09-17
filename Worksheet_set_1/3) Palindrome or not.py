#!/usr/bin/env python
# coding: utf-8

# In[29]:


def test(data):
    return [s == s[::-1] for s in data]
data = ['akshat', 'level', '', 'too', 'balloon']
print("Strings:")
print(data)
print("\nStrings are palindromes or not:")
print(test(data))

