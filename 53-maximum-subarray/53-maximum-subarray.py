class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = 0
        maxsum = -math.inf
        for i in range(len(nums)):
            curr = curr + nums[i]
            maxsum = max(curr, maxsum)
            if curr < 0:
                curr = 0
                continue
        return maxsum