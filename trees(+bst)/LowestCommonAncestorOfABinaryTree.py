# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 2025-07-18

        # basecase: end of tree path
        if root == None:
            return None
        
        # found one of the targets
        if root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # if both are not None, that means a target was found in each side
        if left and right: 
            return root
        
        # if just left is not None, targets were found in the left subtree
        if left:
            return left
        else: # if just right, targets were found in the right subtree
            return right
