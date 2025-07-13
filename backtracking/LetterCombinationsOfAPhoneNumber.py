class Solution:
    #2025-07-09
    def letterCombinations(self, digits: str) -> List[str]:
        res = []

        if digits == "":
            return []

        num_to_letter = {
            "2": 'abc',
            "3": 'def',
            "4": 'ghi',
            "5": 'jkl',
            "6" : 'mno',
            '7': 'prqs',
            '8': 'tuv',
            "9": 'wxyz'
        }

        # i is the index in digits
        def backtrack(i, comb):
            if i == len(digits):
                res.append(comb)
            else:
                for letter in num_to_letter[digits[i]]:
                    comb = comb + letter # add that letter
                    backtrack(i+1, comb) # explore comb
                    comb = comb[: len(comb)-1] # revert change
        backtrack(0, "")
        return res
        