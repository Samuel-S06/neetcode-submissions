# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not p or not q:
            return None

        left = min(p.val, q.val)
        right = max(p.val, q.val)

        current = root

        while current:
            val = current.val
            if left <= val and val <= right:
                return current
            elif left < val and right < val:
                current = current.left
            elif left > val and right > val:
                current = current.right
        
        return None