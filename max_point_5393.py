#!/usr/bin/env python

def get_max_point1(A, k):
    res = 0
    for i in range(k):
        # [-1 -(k-i),-1)
        cur = sum(A[:i]) + sum(A[i-k:])
        res = max(res, cur)
    print 'res', res

def get_max_point2(A, k):
    cur = res = sum(A[:k])
    for i in range(k):
        print A[k -1 -i], A[-1 - i]
        cur -= A[k -1 -i]
        cur += A[-1 - i]
        res = max(res, cur)
    print res
a1 = [1,79,80,1,1,1,200,1]
a2 = [1,1,1,1]
a3 = [1, 3, 5, 7]
a4 = [6,4,2,1]
k = 3
#get_max_point1(a1, k)
#get_max_point1(a2, k)
#get_max_point1(a3, k)
get_max_point2(a3, k)

