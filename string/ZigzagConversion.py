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
        goingDown = False # set to false so trigger down can be set in loop
        # build strings for each row
        while i < len(s):
            rowsStrings[row] += s[i]

            if row == 0:
                goingDown = not goingDown # flip direction
            
            if row == numRows-1:
                goingDown = not goingDown # flip direction
            
            if goingDown:
                row +=1
            else:
                row-=1
            i+=1
        
        # build string
        result = ""
        for string in rowsStrings:
            result += string
    
        return result

            