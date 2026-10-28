# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        levels = {}
        explored = set()
        

        def bfs(root, depth=0):
            lst = levels.get(depth, [])
            lst.append(root.val)
            levels[depth] = lst
            if root.left and root.left not in explored:
                explored.add(root.left)
                bfs(root.left, depth+1)
            if root.right and root.right not in explored:
                explored.add(root.right)
                bfs(root.right, depth+1)

        bfs(root)
        res = []
        for key in sorted(levels.keys()):
            res.append(levels[key])

        return res
