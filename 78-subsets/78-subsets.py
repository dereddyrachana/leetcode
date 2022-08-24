class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        final = []
        
        def backtrack(cur, nums, res):
            final.append(cur)
            for i in range(len(nums)):
                backtrack(cur+[nums[i]],nums[i+1:],res)
        backtrack([],nums,0)
        return final
    
#     class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = []
        
#         def dfs(curr,nums,res):
#             res.append(curr)
#             for i in range(len(nums)):
#                 dfs(curr+[nums[i]], nums[i+1:], res)
                
#         dfs([],nums,res)
#         return res
            