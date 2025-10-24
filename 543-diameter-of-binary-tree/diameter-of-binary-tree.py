# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        best = 0
        def heightofBT(node):
            nonlocal best
            if not node:
                return 0

            height_l = heightofBT(node.left)
            height_r = heightofBT(node.right)
            cd = height_l+height_r

            best = max(best, cd)
            return 1+ max(height_l , height_r)
        

        heightofBT(root)

        return best