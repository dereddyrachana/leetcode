class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen = -1
        l = 0
        for i in nums:
            if i == 0:
                l = 0
                # print(i, l, maxLen)
            else:
                l += 1
                # print(i, l, maxLen)
            maxLen = max(l,maxLen)
        return maxLen