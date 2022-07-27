class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        index = 0
        while index <= high:
            if(nums[index] == 0):
                nums[index], nums[low] = nums[low], nums[index]
                index+=1
                low+=1
            elif(nums[index] == 2):
                nums[index], nums[high] = nums[high], nums[index]
                high-=1
            else:
                index+=1
                
            
        