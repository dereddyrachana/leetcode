# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def recurse_tree(current_node):
            if not current_node:
                return False
            
            left_recurse = recurse_tree(current_node.left)
            right_recurse = recurse_tree(current_node.right)
            
            mid = current_node == p or current_node == q
            
            if mid + left_recurse + right_recurse >= 2:
                self.ans = current_node
            return mid or left_recurse or right_recurse
            
        recurse_tree(root)
        return self.ans
    
            
