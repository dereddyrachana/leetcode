#nums list -> trying to iterate each element
#until count increases
#make a stack -> whenever you see an element higher than this one, pop it
#if stack is empty then return -1
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [0 for i in range(len(nums))]
        for i in range(0,len(nums)):
            res[i] = -1
            for j in range(1,len(nums)):
                if(nums[(i+j) % len(nums)] > nums[i]):
                    res[i] = nums[(i+j) % len(nums)]
                    break
        return res