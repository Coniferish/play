#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
bubble_sort.py : classic bubble sort. 
Time complexity  O(n**2)
"""

__author__ = "John Jennings"

# standard library

# 3rd party packages

# local source

arr = [1,7,5,8,9,3,4,6,2]
print(arr)
n = len(arr)
for i in range(n):
    for j in range (n-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            print("swapped", arr[j], arr[j+1])
print(arr)