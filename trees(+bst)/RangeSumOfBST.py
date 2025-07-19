# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #2025-07-11
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:

        res = 0

        def dfs(node):
            nonlocal res
            if node != None:
                val = node.val
                if val >= low and val <= high:
                    res += val
                # only continue exploring left (lower values) if val is > low
                if val > low:
                    dfs(node.left)
                # only continue exploring right (higher values) if val is still < high
                if val < high:
                    dfs(node.right)

        dfs(root)
        return res        
        
        