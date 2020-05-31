class Solution(object):
    def permuteUnique(self, nums):
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
        traverse = []
        if len(path) == size:
            res.append(path[:])
            return

        for i in range(size):

            if not used[i] and nums[i] not in traverse:
                traverse.append(nums[i])
                used[i] = True
                path.append(nums[i])
                self.get_res(nums, size, used, res, path)
                used[i] = False
                path.pop()

if __name__ == '__main__':
    solution = Solution()
    nums = [1, 1 ,3]
    print solution.permuteUnique(nums)