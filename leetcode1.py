class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        for i,num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i + 1:]):
                if num2 == target - num1:
                    res.append(i)
                    res.append(j + i + 1)
                    break
        return res

    def twoSum2(self, nums, target):
        dic={}
        for k,v in enumerate(nums):
            if target-v in dic:
                return [dic[target-v],k]
            dic[v]=k


s = Solution()
nums = [3,2,4]
target = 6
print s.twoSum(nums, target)
print s.twoSum2(nums, target)