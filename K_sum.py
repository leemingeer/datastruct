#!/usr/bin/env python

class Solution(object):

    def __init__(self, k):
        self.k = k

    def cal_num(self, A, k):
        if len(A) == 0:
            return []
        A.sort()
        for i, a in enumerate(A):
            if a > 0:
                max_sum = sum(A[i:])
                break
        if k >= max_sum:
            return A[i:]
        res = []
        self.get_cal(res, A)

    def get_cal(self, res, A):
        print res, A

        # if A and cur < A[0] or cur == 0:
        #     return cur
        if sum(res) >= self.k:
            return
        for i,a in enumerate(A):
            res.append(a)
            self.get_cal(res, A[i+1:])
            print 'remove', a
            res.remove(a)
        return res

A = [1,2,3,4,5,6]
k = 6
print Solution(k).cal_num(A, k)   