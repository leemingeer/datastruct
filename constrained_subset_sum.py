#!/usr/bin/env python
import collections
import heapq
class Solution(object):

    def constrainedSubsetSum(self, A, k):
        if all([a < 0 for a in A]):
            return max(A)
        n = len(A)
        h = [0]
        lazy = collections.Counter()
        print type(lazy)
        res = 0 
        dp = []
        for i, a in enumerate(A):
            if i > k:
                print dp[i - k -1]
                lazy[dp[i - k -1]] += 1
            while lazy[-h[0]] > 0:
                lazy[-heapq.heappop(h)] -= 1
            cur = a - h[0]
            res = max(res, cur)
            dp.append(cur)
            heapq.heappush(h, -cur)
        return res

A = [10, -2, -10, -5, 20]
k = 2

print Solution().constrainedSubsetSum(A, k)


