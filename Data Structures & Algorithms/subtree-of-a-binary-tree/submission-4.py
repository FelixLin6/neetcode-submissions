# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def treeEq(self, A, B):
        if not A and B or A and not B:
            return False
        return not A and not B or (A.val == B.val and self.treeEq(A.left, B.left) and self.treeEq(A.right, B.right))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.treeEq(root, subRoot):
            return True
        if root:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        return False