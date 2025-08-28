class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        # 2025-08-28
        # need to move through the top row and first column for diagonals

        n = len(grid)
        # diagonals from first row
        for start_col in range(1,n-1): # these diagonals need to be non-decreasing
            col = start_col
            row = 0
            curr = []
            while col < n:
                curr.append(grid[row][col])
                row += 1
                col += 1

            # sort it
            curr.sort()
            col = start_col
            row = 0
            while col < n:
                grid[row][col] = curr[row]
                row +=1
                col +=1

        # diagonals from first columns
        for start_row in range(n):
            curr = []
            col = 0
            row = start_row
            while row < n:
                curr.append(grid[row][col])
                col +=1
                row += 1
            
            curr.sort()
            row = start_row
            col = 0
            while row < n:
                grid[row][col] = curr.pop()
                col +=1
                row += 1

        return grid

