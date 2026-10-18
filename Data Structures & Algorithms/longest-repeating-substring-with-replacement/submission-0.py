class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        if len(s) == 1:
            return 1
        # hashmap of chars with count
        # shrink if length - majoirty > k
        l = 0
        char_map = defaultdict(int)
        max_freq = 0
        max_len = 0

        for i in range(len(s)):
            char_map[s[i]] += 1
            max_freq = max(max_freq, char_map[s[i]])

            while (i - l + 1) - max_freq > k:
                char_map[s[l]] -= 1
                l += 1

            max_len = max(max_len, i - l + 1)

        return max_len





        