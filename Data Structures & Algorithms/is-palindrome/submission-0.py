class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # ignoring left non-alphanum
            while left < right and not s[left].isalnum():
                left += 1

            # ignoring right non-alphanum
            while left < right and not s[right].isalnum():
                right -= 1
            
            if s[left].upper() != s[right].upper():
                return False

            left += 1
            right -= 1
        
        return True
        