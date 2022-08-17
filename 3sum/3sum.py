class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ans = []
        for i in range(0,len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start = i + 1
            end = len(nums)-1
            while start < end:
                t_sum = nums[i] + nums[start] +nums[end]
                if(t_sum == 0):
                    ans.append([nums[i], nums[start], nums[end]])
                    while start < end and nums[start] == nums[start+1]:
                        start+=1
                    while start < end and nums[end] == nums[end-1]:
                        end-=1
                    start+=1
                    end-=1
                elif(t_sum > 0):
                    end-=1
                else:
                    start+=1
        return ans

