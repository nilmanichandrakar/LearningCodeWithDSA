# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        longest= [0]
        def dfs(root):
            if not root:
                return 0
            left_hight= dfs(root.left)
            right_hight= dfs(root.right)
            diameter= left_hight + right_hight
            longest[0]= max(diameter, longest[0])

            return 1+ max(left_hight, right_hight)
        
        dfs(root)
        return longest[0]
        
