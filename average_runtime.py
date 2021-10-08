#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def calculate_average(array):
    #total score
    total = 0
    for number in range(len(array)):
        total += array[number]
    #calculate average of total
    average = total / len(array)
    return average

