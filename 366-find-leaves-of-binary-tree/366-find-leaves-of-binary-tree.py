# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        def helper(node):
            if not node:
                return -1
            left = helper(node.left)
            right = helper(node.right)
            level = max(left,right) + 1
            if(len(result) <= level):
                result.append([])
            result[level].append(node.val)
            return level
        helper(root)
        return result
        
        
                