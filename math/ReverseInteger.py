class Solution:
    def reverse(self, x: int) -> int:

        # 2025-07-15
        
        digits = []
        result = 0

        negative = 1
        if x < 0:
            negative = -1

        while x != 0 :
            print(x)
            dig = x % (negative*10)
            x = int(x / 10)
            digits.append(dig)
        print(digits)
        # go through digits and multiple by tens and add to result
        tens = 1
        while digits:
            dig = digits.pop() * tens
            result += dig
            tens *= 10
        
        if abs(result) > 2**31 -1:
            return 0
        return result

    