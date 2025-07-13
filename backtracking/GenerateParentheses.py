class Solution:
    #2025-07-07
    def generateParenthesis(self, n: int) -> List[str]:
        def isValid(s):
            stack = []
            for p in s:
                if p == "(":
                    stack.append("(")
                else:
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        return False
            return len(stack) == 0
        res = []
        def backtrack(s, open_count, closed_count):
            if len(s) == n*2: # all parentheses added
                if isValid(s):
                    res.append(s)
                    return
            #  try adding open bracket
            if open_count < n:
                s2 = s[:] + "("
                backtrack(s2, open_count+1, closed_count)
            # try adding closed bracket, only if there are more open brackets
            if closed_count < open_count:
                s1 = s[:] + ")"
                backtrack(s1, open_count, closed_count+1)
        backtrack("(", 1, 0)
        return res

                