# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        right_subtree = self.maxDepth(root.right)
        left_subtree = self.maxDepth(root.left)
        max_depth = max(right_subtree,left_subtree)
        
        return max_depth + 1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         if root is None:
#             return 0
#         while root:
#             left_height = self.maxDepth(root.left)
#             right_height = self.maxDepth(root.right)
#             max_depth = max(left_height,right_height)
            
#             return max_depth + 1
            