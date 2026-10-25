# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path1 = []
        path2 = []
        def traverse(root, k, path):
            path.append(root)
            if k.val < root.val:
                traverse(root.left, k, path)
            elif k.val > root.val:
                traverse(root.right, k, path)

        traverse(root, p, path1)
        traverse(root, q, path2)
        print(list(map((lambda x: x.val), path1)))
        print(list(map((lambda x: x.val), path2)))

        i = 0
        while i < min(len(path1), len(path2)) and path1[i] == path2[i]:
            i += 1
        i = max(0, i - 1)
        
        return path1[i]

