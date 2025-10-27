# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        max_node= 0

        def traverse(node, best_seen):
            nonlocal max_node
            if not node:
                return 0
            if node.val >=best_seen:
                max_node+=1
                best_seen = max(best_seen,node.val)
            traverse(node.left, best_seen)
            traverse(node.right,best_seen)

            return max_node

        return traverse(root, root.val)

        

        