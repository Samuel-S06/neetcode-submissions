class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        streak = 0
        maxStreak = 0

        for num in nums:
            if num - 1 not in hashset:
                copy = num
                # inner loop
                while copy in hashset:
                    streak += 1
                    copy += 1
                
            maxStreak = max(maxStreak, streak)
            streak = 0

        return maxStreak
                    

        