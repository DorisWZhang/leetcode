from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 2025-07-20
        
        count = 0
        curr_sum = 0
        prefix = defaultdict(int) # dictionary to track number of times a prefix has appeared (default is 0)
        prefix[0] = 1 # sum of 0 appears once, basecase, subarray 0 to 0

        for num in nums:
            curr_sum += num
            # check if a prefix of currsum-k (difference needed to subtract to get sum of k) exists
            count += prefix[curr_sum - k] 
            # update this prefix sum's # occurrences
            prefix[curr_sum] += 1
        return count


        