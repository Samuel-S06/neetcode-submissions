class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        s = []

        def dfs(s, total, start_idx):
            # BC + Constraint
            if total == target:
                res.append(s[:])
                return
            
            if total > target:
                return
            
            # Choices
            for i in range(start_idx, len(candidates)): # this controls dups in res
                if i > start_idx and candidates[i] == candidates[i - 1]: # this controls dups within candidates + only allows once per element
                    continue
                
                s.append(candidates[i])
                total += candidates[i]
                dfs(s, total, i + 1) # this controls whether we can have unlimited of any single element
                # Undo
                total -= candidates[i]
                s.pop()

        dfs(s, 0, 0)
        return res
        