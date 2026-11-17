class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        subset = []

        def dfs(start_idx):
            res.append(subset[:])
            for i in range(start_idx, len(nums)):
                if i > start_idx and nums[i - 1] == nums[i]:
                    continue
                subset.append(nums[i])
                dfs(i + 1)
                subset.pop()

        dfs(0)
        return res