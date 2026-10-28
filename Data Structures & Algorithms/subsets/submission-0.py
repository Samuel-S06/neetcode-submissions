class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # if index is at a leaf, eturn
            if i > len(nums) - 1:
                res.append(subset.copy())
                return 
                
            # we include this num in the subset
            subset.append(nums[i])
            dfs(i + 1)

            # we exclude this num in the subset
            subset.pop()
            dfs(i + 1)

        dfs(0)

        return res


        