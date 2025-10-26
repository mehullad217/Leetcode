# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True
        if not root:
            return True

        def height(node):
            nonlocal balanced
            if not node:
                return 0
            h_l = height(node.left)
            h_r = height(node.right)
            difference = abs(h_l - h_r)
            if difference>1:
                balanced = False


            node_height = 1+max(h_l,h_r)

            return node_height

        height(root)

        return balanced








       

        
    