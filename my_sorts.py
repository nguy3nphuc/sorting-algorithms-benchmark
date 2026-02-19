import numpy as np
import time
import random

def heapify(arr, n, i):
    '''
    Docstring for heapify
    
    :param arr: The array to be heapified
    :param n: The size of the heap
    :param i: The index of the root element of the subtree
    '''
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def partition(arr, start, end):
    if start < end: 
        random_pivot_idx = random.randint(start, end)
        arr[random_pivot_idx], arr[end] = arr[end], arr[random_pivot_idx]

    pivot_val = arr[end] 
    i = start - 1
    for j in range(start, end):
        if arr[j] <= pivot_val: 
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[end] = arr[end], arr[i + 1]
    return i + 1

def _quick_sort_recursive(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        _quick_sort_recursive(arr, start, pivot - 1)
        _quick_sort_recursive(arr, pivot + 1, end)

def quick_sort(arr):
    _quick_sort_recursive(arr, 0, len(arr) - 1)

def merge_sort(arr):
    n = len(arr)
    if(n <= 1): return
    left = arr[ :n//2]
    right = arr[n//2: ]
    merge_sort(left)
    merge_sort(right)
    merge(left, right, arr)

def merge(left, right, arr):
    l_size = len(left)
    r_size = len(right)
    n = len(arr)
    i = l = r = 0
    while l < l_size and r < r_size:
        if(left[l] < right[r]):
            arr[i] = left[l]
            i += 1
            l += 1
        else:
            arr[i] = right[r]
            i += 1
            r += 1
    while l < l_size:
            arr[i] = left[l]
            i += 1
            l += 1
    while r < r_size:
            arr[i] = right[r]
            i += 1
            r += 1

if __name__ == "__main__":
    arr = [10, 30, 20, 100, 40, 50, 60, 80, 70, 90]
    #heap_sort(arr)
    #quick_sort(arr, 0, len(arr) - 1)
    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    print(f"Heap Sort took {end_time - start_time:.5f} seconds")
    print(arr)

