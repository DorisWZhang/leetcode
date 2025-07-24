class Solution:
    def jump(self, nums: List[int]) -> int:
        # 2025-07-23
        # dp problem
        # state variables:
        # i - index in nums
        
        # data structure
        # memo[i] - min jumps to get to index i

        # base case
        # i >= len(nums)

        # recurrence relation
        # 1 (to account for current jump ) + jump(i + size) (to account for future jumps)
        memo = {} 
        n = len(nums)

        if n == 1:
            return 0

        def jump(i):
            if i >= n-1:
                return 0
            if i not in memo:
                minJumps = float('inf')
                for size in range(1,nums[i]+1):
                    # add previous jumps, plus 1 jump for this turn + recursive call for future jumps
                    minJumps = min(1 + jump(i + size), minJumps)
                memo[i] = minJumps
            return memo[i]

        return jump(0)
