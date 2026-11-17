class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []

        def dfs(p):
            if len(perm) == len(nums):
                res.append(p[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in p:
                    p.append(nums[i])
                    dfs(p)
                    p.pop()

        dfs(perm)

        return res



        