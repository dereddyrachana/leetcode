class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """    
        if not p and not q:
            return True
        if not q or not p:
            return False
        if p.val != q.val:
            return False
        leftsubTree = self.isSameTree(p.left,q.left)
        rightsubTree = self.isSameTree(p.right,q.right)
        return leftsubTree and rightsubTree
    
    
#         return True
        # # p and q are both None
        # if not p and not q:
        #     return True
        # # one of p and q is None
        # if not q or not p:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)