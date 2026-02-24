# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node, val):
            if not node:
                return 0
            val = (val << 1) | node.val
            return val if node.left == node.right else dfs(node.left, val) + dfs(node.right, val)
        return dfs(root, 0)
