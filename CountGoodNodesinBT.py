# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root: TreeNode, mx_val: int):
            if root is None:
                return
            nonlocal ans
            if mx_val <= root.val:
                ans += 1
                mx_val = root.val
            dfs(root.left, mx_val)
            dfs(root.right, mx_val)

        ans = 0
        dfs(root, -1000000)
        return ans
