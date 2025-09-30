class Solution:
    def reverse(self, x: int) -> int:
        # 2025-09-29

        result = 0
        if x > 0:
            sign = 1
        else:
            sign = -1
        
        x = abs(x)

        while x:
            digit = x % 10
            x = x // 10 # update x to get rid of last digit
            result = result*10 + digit
            if result > 2**31 -1:
                return 0
        
        return sign*result