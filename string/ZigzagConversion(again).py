class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 2025-09-28
        # each row is like its own "word"
        if numRows == 1:
            return s

        rowWords = [""] * numRows

        direction = -1 # flip it when you each row == 0 or row == numRows-1
        currRow = 0

        for letter in s:
            rowWords[currRow] += letter
            if currRow == 0 or currRow == numRows-1:
                direction = -direction
            currRow += direction
        
        # now we have the words created in each row
        result = ""
        for word in rowWords:
            result += word
        
        return result
