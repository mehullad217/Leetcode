# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        stk = [(root,1)]
        max_depth=0
        while stk:
            node_tup = stk.pop()
            node=node_tup[0]
            max_depth = max(max_depth, node_tup[1])
            if node.right:
                stk.append((node.right,node_tup[1]+1))
            if node.left:
                stk.append((node.left,node_tup[1]+1))
                

        return max_depth

     
        