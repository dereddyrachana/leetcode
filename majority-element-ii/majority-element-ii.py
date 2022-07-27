class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        l = len(nums)
        d = {}
        for i in range(l):
            if nums[i] not in d:
                d[nums[i]] = 1
            else:
                d[nums[i]]+=1
        # print(d)
        floor_num = floor(l/3)
        # print(floor_num)
        ans = []
        for i,row in d.items():
            # print(i)
            if d[i] > floor_num:
                ans.append(i)
        # print(ans)
        return ans
                
            