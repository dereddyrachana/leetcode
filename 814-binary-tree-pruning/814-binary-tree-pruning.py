# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# traverse through the tree
#if you find any node not equal to one and no children node.left and node.right ==0
#remove that node
#
#
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left = self.pruneTree(root.left)
            root.right = self.pruneTree(root.right)
            if(root.left == None and root.right == None and root.val != 1):
                return None
            else:
                return root
        
                
        
                    
                    
        