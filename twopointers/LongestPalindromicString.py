class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 2025-09-24
        def isPalindrome(s):
            return s == s[::-1]

        maxLen = 1
        longest = s[0]
        n = len(s)

        for i in range(n):
            for j in range(n-1, i, -1): 
                if j-i+1 < maxLen: # cannot be longer than maxLen
                    break
                if s[i] == s[j]: # same end letters, check the rest!
                    if isPalindrome(s[i:j+1]):
                        longest = s[i:j+1]
                        maxLen = len(longest)
        return longest

        