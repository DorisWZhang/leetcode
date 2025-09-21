class Solution:
    def isValid(self, s: str) -> bool:
        # 2025-09-17

        stack = []
        brackets = {
            "(": ")",
            "{": "}",
            "[": ']'
        }

        for b in s:
            if b in brackets:
                stack.append(b)
            else:
                if not stack:
                    return False
                openB = stack.pop()
                if brackets[openB] != b:
                    return False
        
        return len(stack) == 0
