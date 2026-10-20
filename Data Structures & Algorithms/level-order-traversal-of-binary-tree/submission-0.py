# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque()
        binary_list = []
        q.append(root)

        def bfs(q):
            while q:
                num = len(q)
                layer_list = []
        
                for _ in range(num):
                    node = q.popleft()
                    if node:
                        layer_list.append(node.val)

                        q.append(node.left)
                        q.append(node.right)
                if len(layer_list) != 0:
                    binary_list.append(layer_list)

        
        bfs(q)

        return binary_list

        
        
        