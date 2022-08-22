class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def dfs(curr,nums,res):
            res.append(curr)
            for i in range(len(nums)):
                dfs(curr+[nums[i]], nums[i+1:], res)
                
        dfs([],nums,res)
        return res
            