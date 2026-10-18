class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        if len(s) == 1:
            return 1

        l = 0
        char_map = defaultdict(int)
        max_freq = 0
        max_len = 0

        for r in range(len(s)):

            # Expand: r += 1, char_map increase, max_freq
            char_map[s[r]] += 1
            max_freq = max(max_freq, char_map[s[r]])

            # Shrink
            while (r - l + 1) - max_freq > k:
                char_map[s[l]] -= 1
                l += 1
            
            # Record
            max_len = max(max_len, r - l + 1)

        return max_len





        