# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Case 1: root is not None and subRoot is None
        # Case 2: root is None (both subcases result in False)
        # Case 3: subRoot and root are the Same --> run isSameTree
        # Case 4: subRoot and root are not the same --> skip

        # Case 1
        if root is not None and subRoot is None:
            return True

        # Case 2
        if root is None:
            return False

        # Case 3
        if subRoot.val == root.val:
            if self.isSameTree(root, subRoot) is True:
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if p is None and q is None:
            return True
        
        if (p is None and q is not None) or (p is not None and q is None):
            return False
        
        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


        