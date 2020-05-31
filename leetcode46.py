#!/usr/bin/env python

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        if size == 0:
            return []
        
        res = []
        path = []
        used = [False] * size
        self.get_res(nums, size, used, res, path)
        return res

    def get_res(self, nums, size, used, res, path):
        if len(path) == size:
            res.append(path[:])
            return
        for i in range(size):
            if not used[i]:
                used[i] = True
                path.append(nums[i])
                self.get_res(nums, size, used, res, path)
                used[i] = False
                path.pop()

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2 ,3]
    print solution.permute(nums)