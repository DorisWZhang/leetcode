class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # 2025-08-16

        result = []

        # backtracking (all possible)
        # put closing brackets on the stack
        # i == num of open brackets left
        def backtrack(curr, i, stack):
            if i == 0:
                while stack:
                    curr += stack.pop()
                result.append(curr)
            else:
                # either add open bracket
                copy_stack = stack[::]
                copy_stack.append(")")
                copy_curr = curr[::]
                copy_curr += "("
                backtrack(copy_curr, i-1, copy_stack)
                # if there are closed brackets on stack, try adding close bracket
                if stack:
                    copy_curr2 = curr[::]
                    copy_curr2 += stack.pop()
                    backtrack(copy_curr2, i, stack)
        backtrack("", n, [])
        return result