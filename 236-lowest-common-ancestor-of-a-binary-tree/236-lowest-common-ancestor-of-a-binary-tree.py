# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = []
        def dfs(node):
            if not node:
                return False
            left = dfs(node.left)
            right = dfs(node.right)
            cur = p == node or q == node
            if(left and right) or (left and cur) or (right and cur):
                self.ans = node
                return
            return left or right or cur
        dfs(root)
        return self.ans
            
            
                
            
            