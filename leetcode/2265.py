# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        def f(n):
            if n is None:
                return 0, 0, 0
            t1, c1, b1 = f(n.left)
            t2, c2, b2 = f(n.right)
            t = t1 + t2 + n.val
            c = c1 + c2 + 1
            b = 1 if n.val == t // c else 0
            return t, c, b1 + b2 + b
        t, c, b = f(root)
        return b
