class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        # 2025-07-24
        # prefix sum
        # loop through, check if by subtracting any previous prefix sums it will ==k or if curr_sum == k
        # track current max size
        maxSize = 0
        prefix_sum = {} # dict of amount: index (only consider the first occurrence of a prefix sum value)
        # this is because we want hte max subarray, so we want to take out the least length
        curr_sum = 0
        
        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum not in prefix_sum:
                prefix_sum[curr_sum] = i
            # if curr_sum == k, this is the longest subarray we'veseen so far, automatcally set to maxSize
            if curr_sum == k:
                maxSize = i+1
            # see if a subarray can be made somewhere between 0 and i whose sum == k
            elif curr_sum-k in prefix_sum:
                maxSize = max(i - prefix_sum[curr_sum-k], maxSize)
        return maxSize



        