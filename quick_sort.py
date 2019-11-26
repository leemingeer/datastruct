#!/usr/bin/env python

def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid = arr[len(arr)//2]
    #remove operation affects this origin data this is 
    #address operate on the save memory address
    arr.remove(mid)
    left, right = [], []
    for i in arr:
        if i < mid:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [mid] + quick_sort(right)
        
oneline_quick_sort = lambda arr: arr if len(arr) <=1 else oneline_quick_sort(
    [item for item in arr[1:] if item <= arr[0]]) + \
    [arr[0]] + oneline_quick_sort([item for item in arr[1:] if item > arr[0]])

if __name__ == "__main__":
    arr = [11,32,15,67,21]
    print("current arr:", arr)
    print(quick_sort(arr))
    print("current arr:", arr)
    print(oneline_quick_sort(arr))