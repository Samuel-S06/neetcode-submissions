class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        repeat = set()
        l, r = 0, 0
        length = 0

        for char in s:
            while char in repeat:
                repeat.remove(s[l])
                l += 1
            
            repeat.add(char)
            r += 1

            length = max(length, r - l)
        
        return length
        
        