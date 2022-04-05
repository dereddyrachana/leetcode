class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        p1 = 0
        p2 = len(nums) -1
        while(p1!=p2):
            if(nums[p1]+nums[p2]>target):
                p2 = p2-1
            elif(nums[p1] + nums[p2] < target):
                p1 = p1+1
            else:
                return [p1+1,p2+1]