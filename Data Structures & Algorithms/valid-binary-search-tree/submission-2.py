# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        def helper(root: Optional[TreeNode], lo, hi) -> bool:
            if not root: return True

            if not lo < root.val < hi: return False
            if root.left and root.left.val >= root.val: return False  
            if root.right and root.right.val <= root.val: return False

            return helper(root.left, lo, root.val) and helper(root.right, root.val, hi)

        return helper(root, float('-inf'), float('inf'))
