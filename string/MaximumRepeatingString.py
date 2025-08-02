class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # 08-02-2025
        # substring
        # if word not in sequence, return 0
        # k is at least 1,
        # continue checking multiples of word is in sequence and return the highest multiple k

        if word not in sequence:
            return 0
        else:
            k = 0
            word_repeated = word
            while word_repeated in sequence:
                k+=1
                word_repeated += word
            return k