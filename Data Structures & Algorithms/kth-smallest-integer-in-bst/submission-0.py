# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # base case

        def dfs(node):
            #BC
            if not node:
                return []
            
            if not node.left and not node.right:
                return [node.val]
            
            return dfs(node.left) + [node.val] + dfs(node.right)

        output_list = dfs(root)

        return output_list[k-1]


        



        