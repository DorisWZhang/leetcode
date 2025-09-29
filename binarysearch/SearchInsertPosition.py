class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 2025-09-28
        # binary search

        lo = 0
        hi = len(nums)-1

        while lo <= hi:
            mid = (lo+hi) // 2
            num = nums[mid]
            if num == target:
                return mid
            elif num > target:
                hi = mid-1
            else: #
                lo = mid+1
        # return lo
        # if lo is smaller than everything lo = 0
        # if lo is bigger than everything lo = len(nums)
        # if lo is somewhere in the middle, lo points to first element GREATER than target
        return lo


        