# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        good_nodes = 0
        maxVal = root.val
        
        def dfs(root, maxVal):
            nonlocal good_nodes

            if root.val >= maxVal:
                good_nodes += 1
            
            maxVal = max(maxVal, root.val)

            if root.right:
                dfs(root.right, maxVal)
            if root.left:
                dfs(root.left, maxVal)

        dfs(root, maxVal)

        return good_nodes
        