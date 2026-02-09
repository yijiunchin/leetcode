# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        vals = []
        def inorder(node):
            if node:
                inorder(node.left)
                vals.append(node.val)
                inorder(node.right)
        inorder(root)

        def build(l, r):
            if l > r: return None
            mid = (l + r) // 2
            return TreeNode(vals[mid], build(l, mid - 1), build(mid + 1, r))

        return build(0, len(vals) - 1)
