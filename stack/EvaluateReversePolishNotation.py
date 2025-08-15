class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # 2025-08-15

        stack = []
        operators = '+-*/'
        for t in tokens:
            if t not in operators:
                stack.append(int(t))
            else: # if it's an operator perform with two latest ints
                num2 = stack.pop()
                num1 = stack.pop()
                if t == '+':
                    result = num1 + num2
                elif t == '-':
                    result = num1 - num2
                elif t == '*':
                    result = num1 * num2
                else:
                    result = int(num1 / num2)
                stack.append(result)
        return stack.pop()