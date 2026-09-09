# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        minVal = float("-inf")
        maxVal = float("inf")

        return self.isNodeValid(root, minVal, maxVal)


    def isNodeValid(self, node: Optional[TreeNode], low: float, high: float) -> bool:

        # Case 1: node is None --> True
        if node is None:
            return True

        # Case 2: node.val < low --> False
        # Case 3: node.val > high --> False
        if node.val <= low or node.val >= high:
            return False

        # Case 4: low < node.val < high --> continue
        return self.isNodeValid(node.left, low, node.val) and self.isNodeValid(node.right, node.val, high)



        