class Solution:
    def countAndSay(self, n: int) -> str:
        # 2025-07-16
        if n == 1:
            return '1'
        else:
            RLE = self.countAndSay(n-1)
            count = 0
            prev = " "
            result = ""
            for char in RLE:
                if char != prev:
                    if count == 0:
                        count += 1
                        prev = char
                    else: # end of a repeated number, add count + previous number
                        result += str(count)
                        result += prev
                        # restart count and number to current char
                        prev = char
                        count = 1
                else: 
                    count += 1
            result += str(count)
            result += RLE[-1]
            return result
