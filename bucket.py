# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 08:52:46 2023

@author: Hannah
"""
from bubbles import bubbleSort

def bucketSort(array):
    bucket = []

    # Create empty buckets
    for i in range(len(array)):
        bucket.append([])

    # Insert elements into their respective buckets
    for j in array:
        index_b = int(0.1 * j)
        if index_b >= len(bucket):
            index_b = len(bucket) - 1
        bucket[index_b].append(j)

    # Sort the elements of each bucket
    for i in range(len(array)):
        bubbleSort(bucket[i])

    # Get the sorted elements
    k = 0
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

