class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 2025-07-26
        # really just moving up and down rows and adding letter to that row's string thats being built

        # edge case:one row
        if numRows == 1:
            return s

        rowsStrings = [""] * numRows # start a word for each row
        row = 0 # track current row
        i = 0
        direction = -1 # set it to go up, so first iteration will flip it
        # build strings for each row
        for letter in s:
            rowsStrings[row] += letter

            if row == 0 or row == numRows-1:
                direction = -direction

            row += direction
            
        # build string
        result = ""
        for string in rowsStrings:
            result += string
    
        return result