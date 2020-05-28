#!/usr/bin/env python

class Solution(object):

    def combinationSum(self, A, k):
        if len(A) == 0:
            return []
        A.sort()
        path = []
        res = []
        self.get_path(A, k, path, res)
        return res

    def get_path(self, A, t, path, res):
        if t == 0:
            res.append(path[:])
            return
        for i, a in enumerate(A):
            target = t - a
            if target < 0:
                return
            path.append(a)
            self.get_path(A[i:], target, path, res)
            r = path.pop()


if __name__ == '__main__':
    solution = Solution()
    A = [2,3,6,7]
    k = 7
    print solution.combinationSum(A, k)