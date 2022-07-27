class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        #print(nums)
        min_sum = float('inf')
        for i in range(len(nums)):
            low = i+1
            high = len(nums) - 1
            while low < high:
                t_sum = nums[i] + nums[low] + nums[high]
                #print("t_sum",t_sum)
                if abs(target - t_sum) < abs(min_sum):
                    min_sum = target - t_sum
                # min_sum = min(min_sum,target - t_sum)
                if(t_sum < target):
                    low +=1
                else:
                    high -=1
            if min_sum ==0 :
                break
        return target - min_sum