#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
selectionsort.py : classic selection sort. 
Time complexity:
Worst: O(n**2)
Best: O(n**2)
Space Complexity: O(1)
"""

__author__ = "John Jennings"

# standard library

# 3rd party packages

# local source

arr = [8,7,5,6,4,3,2,1]
n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i, n, 1):
        if arr[j] < arr[min_index]:
            min_index = j

    arr[i], arr[min_index] = arr[min_index], arr[i]
    print(arr)