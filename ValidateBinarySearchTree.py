# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stc = [(root,float('-inf'),float('inf'))]
      
        while stc:
            node, minn, maxx = stc.pop()

            if node.val<= minn or node.val>= maxx:
                return False
            else:
                if node.left:
                    stc.append((node.left, minn, node.val))

                if node.right:
                    stc.append((node.right,node.val,maxx))
        return True
        
