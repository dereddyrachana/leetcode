class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
            for i in range(first,n+1):
                curr.append(i)
                backtrack(i+1,curr)
                curr.pop()
        output = []
        backtrack()
        return output      
        
#         def backtrack(first = 1, curr = []):
#             # if the combination is done
#             if len(curr) == k:  
#                 output.append(curr[:])
#             for i in range(first, n + 1):
#                 # add i into the current combination
#                 curr.append(i)
#                 # use next integers to complete the combination
#                 backtrack(i + 1, curr)
#                 # backtrack
#                 curr.pop()
        
#         output = []
#         backtrack()
#         return output
        
                
                
        