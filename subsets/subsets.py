class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(arr,nums,res):
            res.append(arr)
            for i in range(len(nums)):
                dfs(arr + [nums[i]],nums[i+1:], res)
                
        dfs([],nums,res)
        return(res)
        
        
        
        
        
        
# def subsets(self, nums):
#         ret = []
#         self.dfs(nums, [], ret)
#         return ret
    
#     def dfs(self, nums, path, ret):
#         ret.append(path)
#         for i in range(len(nums)):
#             self.dfs(nums[i+1:], path+[nums[i]], ret)