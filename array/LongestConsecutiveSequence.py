class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # 2025-08-07

        # only look at numbers that start a sequence, num-1 does not exist
        # we only care about unique nums, and don't care about order

        nums_set = set(nums)
        longest = 0
        n = len(nums)

        for num in nums_set: 
            if num-1 not in nums_set: # starts a sequence
                curr_length = 1
                while num+1 in nums_set:
                    curr_length += 1
                    num+=1
                longest = max(curr_length, longest)
        return longest