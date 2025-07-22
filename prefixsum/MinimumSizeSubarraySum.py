
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # 2025-07-21
        # prefix sum
        curr_sum = 0
        prefix_sum = [-1] * (len(nums) +1)
        minLen = float('inf')
        for i, num in enumerate(nums):
            curr_sum += num
            prefix_sum[i+1] = curr_sum
            
            if curr_sum >= target:
                # binary search to find the highest index, whose number when subtracted from curr_sum still >= target
                lo, hi = 0, i + 1
                needed = curr_sum - target

                while lo < hi:
                    mid = (lo + hi) // 2
                    if prefix_sum[mid] <= needed:
                        lo = mid + 1
                    else:
                        hi = mid
                j = lo - 1
                if j >= 0:
                    minLen = min(minLen, i - j + 1)
        return 0 if minLen == float('inf') else minLen 