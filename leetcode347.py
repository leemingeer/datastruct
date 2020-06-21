#!/usr/bin/env python

# top k element
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n_f = dict()
        f_n = dict()
        if k > len(nums):
            return []
        for n in nums:
            n_f[n] = n_f.setdefault(n, 0) + 1

        for n, f in n_f.items():
            if f not in f_n:
                f_n[f] = [n]
            else:
                f_n[f].append(n)
        print 'f_n',f_n
        res = []
        for i in range(len(nums), 0, -1):
            if i in f_n:
                for item in f_n[i]:
                    res.append(item)
                    if len(res) == k:
                        return res
        return res

nums = [2,5,2,7,1,5,3,8,2]
solution = Solution()
print solution.topKFrequent(nums, 3)