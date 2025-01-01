#!/usr/bin/env python
# coding: utf-8

# Problem. Define make_count_dictionary in HW0.py
# In a separate file named HW0.py (please do not use a different name), write the function make_count_dictionary that takes a list L and returns a dictionary D where:
# 
# The keys of D are the unique elements of L (i.e., each element of L appears only once).
# The value D[i] is the number of times that i appears in list L.
# Your code should work for lists of strings, lists of integers, and lists containing both strings and integers.
# 
# For example:
# 
# # input
# L = ["a", "a", "b", "c"]
# # output
# {"a" : 2, "b" : 1, "c" : 1}
# 
# For this homework, you don’t need to mention this task in your blog.

# In[17]:


def make_count_dictionary(L):
    D ={i:L.count(i) for i in L}
    return D


# In[18]:


L = ["a", "a", "b", "c"]
make_count_dictionary(L)

