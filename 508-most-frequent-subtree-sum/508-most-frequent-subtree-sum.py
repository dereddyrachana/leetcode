# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#dictionary to keey count
#bottom-up approach -> sum for each tree and add to the counts
        
        
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        counts = dict()
        if not root:
            return []
        def cal_sum(node):
            if not node: 
                return 0
            sum_val = node.val + cal_sum(node.left) + cal_sum(node.right)
            if sum_val not in counts:
                counts[sum_val] = 1
            else:
                counts[sum_val] += 1
            return sum_val
        cal_sum(root)
        max_value = max(counts.values())
        # print(max(counts.values()))
        for key, value in counts.items():
            return [key for key, value in counts.items() if value == max_value]
        # for key, value in counts.items():
        #     get_max = max(counts.values())
        #     print(get_max)
        return 
        print(counts)
                
        