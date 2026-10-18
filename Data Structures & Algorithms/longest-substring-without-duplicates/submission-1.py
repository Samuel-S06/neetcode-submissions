class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        l = 0
        max_len = 0
        char_set = set()

        for r in range(len(s)):
            # 1.) Expand: r += 1

            # 2.) Shrink
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
                            
            # 3.) Record
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len


        