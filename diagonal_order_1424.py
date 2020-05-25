#!/usr/bin/env python

class Solution(object):
    def findDiagonalOrder(self, A):
        res = []
        for i,r in enumerate(A):
            for j,a in enumerate(r):
                if i + j >= len(res):# len(res) is the next index of i+j
                    res.append([])
                res[i + j].append(a)
        res2 = []
        for k, c1 in enumerate(res):
            res2.extend(c1[::-1])
        print res2
A1= [[1,2,3], [4],[5,6,7],[8],[9,10,11]]
Solution().findDiagonalOrder(A1)