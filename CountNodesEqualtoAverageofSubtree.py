# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        nodes = [0]
        def sumNodes(root):
            if not root:
                return (0, 0)
            Node_left, sum_left = sumNodes(root.left)
            Node_right, sum_right = sumNodes(root.right)
            #count total no of nodes in tree
            N = 1 + Node_left + Node_right
            #Sum of all nodes value
            sum = root.val + sum_left + sum_right
            avg = sum // N

            if root.val == avg:
                nodes[0] += 1
            
            return (N, sum)

        sumNodes(root)
        return  nodes[0]
        
