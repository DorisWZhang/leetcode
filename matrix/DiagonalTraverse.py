class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # 2025-09-24
        m = len(mat)
        n = len(mat[0])
        result = []
        row = 0
        col = 0
        up = True # flag to know which direction
        # up means, up and right, down means down and left
        while len(result) < m*n:
            result.append(mat[row][col])

            if up:
                if row == 0 and not col == n-1: # hit top edge, move to the right
                    col +=1
                    up = False
                elif col == n-1: # hit right edge, move down
                    row +=1
                    up = False
                else: # regular movement through diagonal
                    row -= 1
                    col += 1
            else:
                if col == 0 and not row == m-1: # hit left edge, move down
                    row += 1
                    up = True
                elif row == m-1: # hit bottom edge, move right
                    col +=1 
                    up = True
                else: # regular down left movement
                    col -=1
                    row +=1
        return result
        