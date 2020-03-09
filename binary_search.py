#!/usr/bin/env python
# 1. sorted, descend or upscend
# 2. bounded
# 3. could access by index

#>>> (2 + 4)/2
#3
#>>> (2 + 5)/2
#3
#>>> (2 + 5.5)/2
#3.75
#>>> (2 + 5.5)//2
#3.0
#>>> (2 + 4)//2
#3


def binary_search(array, target):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = left + (right - left)/2
        print 'left mid right',left, mid, right
        if array[mid] == target:
            return array.index(target)
        elif array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    print 'not found'

if __name__ == '__main__':
    arr_odd = [1,3,6,8,12,15,23]
    print binary_search(arr_odd, 23)
    arr_pair = [1,3,6,8,12,15,23,45]
    print binary_search(arr_pair,23)

    arr_odd = [1,3,6,8,12,15,23]
    print binary_search(arr_odd, 9)

#output
#left mid right 0 3 6
#left mid right 4 5 6
#left mid right 6 6 6
#6
#left mid right 0 3 7
#left mid right 4 5 7
#left mid right 6 6 7
#6
#left mid right 0 3 6
#left mid right 4 5 6
#left mid right 4 4 4
#not found
#None