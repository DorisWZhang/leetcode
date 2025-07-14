class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 2025-07-14

        substring = ""
        maxlen = 0
        currlen = 0
        start = 0
        end = 0
        while end < len(s):
            letter = s[end]
            if letter not in substring:
                substring += letter
                currlen += 1
            else: # if next added letter already in letters, start new substring
                maxlen = max(maxlen, currlen) # update max length
                while s[start] != letter:
                    start +=1
                start+=1 # skip the first occurrence of the letter
                substring = s[start:end+1]
                currlen = end-start +1
            end += 1
        return max(maxlen, currlen)