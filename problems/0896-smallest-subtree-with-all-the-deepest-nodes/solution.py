# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if node is None:
                return 0, None

            depth_l, node_l = dfs(node.left)
            depth_r, node_r = dfs(node.right)

            if depth_l > depth_r:
                return depth_l + 1, node_l
            if depth_l < depth_r:
                return depth_r + 1, node_r
            return depth_l + 1, node

        return dfs(root)[1]

