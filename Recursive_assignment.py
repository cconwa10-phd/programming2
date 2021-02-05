#!/usr/bin/env python
# coding: utf-8

# Recursive_Assignment cconwa10@uncc.edu

# Call function and define list

# In[4]:


list_sum = [1, 2, [3,4], [5,6]]
recur_func(list_sum)


# Function that sums the list recursively

# In[2]:


def recur_func(list_sum):
    sum = 0
    for i in list_sum:
        if type(i) == type([]):
            sum = sum + recur_func(i)
        else:
            sum = sum + i        
    return sum

