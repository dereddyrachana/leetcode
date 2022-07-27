class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if(i not in nums):
                return i
        return l
                