class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2025-09-28
        # given a state, try all paths and append to result (backtracking)

        result = []

        def backtrack(path, numOpen, numClosed):
            if numOpen == n and numClosed == n:
                result.append(path)
            else:
                if numOpen < n:
                    backtrack(path+'(', numOpen+1, numClosed)
                if numClosed < numOpen: # can only place another numClosed if there are less
                # this conditional ensures we create valid parentheses
                    backtrack(path+')', numOpen, numClosed+1)
        
        backtrack("", 0, 0)
        return result
                