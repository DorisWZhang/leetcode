class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # substring of len 3 of num, sliding window to find the max, 
        # contains only one unique int

        left = 0
        right = 3
        maxNum = "0"
        while right <= len(num):
            currNum = num[left:right]
            if len(set(currNum)) == 1: # unique nums
                numVal = int(currNum)
                if numVal >= int(maxNum):
                    maxNum = str(currNum)
            left+=1
            right +=1
        
        if maxNum == "0": # no possible good num
            return ""
        return maxNum