class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq, s2_freq = [0] * 26, [0] * 26

        # Initialize freq tables
        for i in range(len(s1)):
            s1_freq[ord(s1[i]) - ord("a")] += 1
            s2_freq[ord(s2[i]) - ord("a")] += 1

        matches = 0

        # Get initial match count
        for i in range(26):
            if s1_freq[i] == s2_freq[i]:
                matches += 1
        if matches == 26:
            return True
        
        # Iterate as long as matches < len(s1)

        l = 0

        for r in range(len(s1), len(s2)):
            # Handling right pointer
            r_index = ord(s2[r]) - ord('a')

            if s2_freq[r_index] == s1_freq[r_index]: # if match before increasing right
                matches -= 1
            s2_freq[r_index] += 1
            if s2_freq[r_index] == s1_freq[r_index]: # if match after increasing right
                matches += 1

            # Handling left pointer
            l_index = ord(s2[l]) - ord('a')

            if s2_freq[l_index] == s1_freq[l_index]: # if match before increasing left
                matches -= 1
            s2_freq[l_index] -= 1
            if s2_freq[l_index] == s1_freq[l_index]: # if match after increasing left
                matches += 1

            l += 1

            # Final Check
            if matches == 26:
                return True
            
        return False
            







        
        