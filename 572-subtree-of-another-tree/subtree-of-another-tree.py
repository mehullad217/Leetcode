# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True          
        if not root:
            return False 

        def sametree(p,q):
            if not p and not q:
                return True


            if (not p and q) or (p and not q):
                return False


            if p.val != q.val:
                return False

            return sametree(p.left,q.left) and sametree(p.right,q.right) 

        
        return sametree(root, subRoot)or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

        


        


        




            


            