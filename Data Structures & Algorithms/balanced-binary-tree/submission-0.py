# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # height helper: recursively get height of node
        def getHeight(node):
            if not node:
                return 0

            return 1 + max(getHeight(node.left), getHeight(node.right))

        if not root:
            return True

        leftHeight = getHeight(root.left)
        rightHeight = getHeight(root.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        # starting at root, downwards --> every single node that to be balanced until we reach leaf nodes
        return self.isBalanced(root.left) and self.isBalanced(root.right)

        
        