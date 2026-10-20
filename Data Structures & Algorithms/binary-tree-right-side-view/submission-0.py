# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque()
        final_list = []
        q.append(root)

        def bfs(q):
            while q:
                num = len(q)
                right_num = float("inf")

                for i in range(num):
                    node = q.popleft()
                        
                    if i == num - 1:
                        right_num = node.val

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
                
                                            
                if right_num != float("inf"):
                    final_list.append(right_num)
        
        bfs(q)

        return final_list

        