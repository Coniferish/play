#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bubble_sort.py : classic bubble sort. 
Time complexity:
Worst: O(n**2)
Best: O(n)
Space Complexity: O(1)
"""

__author__ = "John Jennings"

# standard library

# 3rd party packages

# local source

arr = [3,7,8,57,5,234,1,2,6,9]
n = len(arr)
for i in range(n):
    swapped = False
    for j in range(n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            swapped = True
    if swapped == False:
        print('break')
        break
print(arr)
