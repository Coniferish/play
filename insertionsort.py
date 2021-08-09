#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
insertionsort.py : insertion sort. 
Time complexity:
Worst: O(n**2)
Best: O(n)
Space Complexity: O(1)
"""

__author__ = "John Jennings"

# standard library

# 3rd party packages

# local source

arr = [132,245,635,6857,987,2,34,5,6,1]
n = len(arr)
for i in range(1, n, 1): # start on the second number (index 1)
    j = i
    while j > 0 and arr[j] < arr[j-1]: 
        arr[j], arr[j-1] = arr[j-1], arr[j] 
        j = j - 1 # keep moving the current number down until it's in the correct place
print(arr)