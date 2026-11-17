class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sums = []
        total = 0

        def dfs(sums, start_idx, total):
            # BC 1
            if total == target:
                res.append(sums[:])
                return
            
            # BC 2 + Constraint
            if total > target:
                return
            
            # Choices
            # the bounding prevents dups
            for i in range(start_idx, len(nums)):
                # Constraint
                sums.append(nums[i])
                total += nums[i]
                dfs(sums, i, total)
                # Undo
                sums.pop()
                total -= nums[i]   
                   
        dfs(sums, 0, total)
        return res
        