# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, s):
            if node is None:
                return 0
            s += node.val
            res = cnt[s - targetSum]
            cnt[s] += 1
            res += dfs(node.left, s)
            res += dfs(node.right, s)
            cnt[s] -= 1
            return res

        cnt = Counter({0: 1})
        return dfs(root, 0)
